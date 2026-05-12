---
name: wordpress-hardening
description: Detect and contain WordPress compromises, then harden the install against re-entry. Covers webshell detection across the Sid Gifari, WSO, FilesMan, b374k and c99 families, backdoored mu-plugins, malicious admin accounts, and shared-hosting lateral-movement defense. Invoke when a WordPress site shows unexpected files, suspicious admin accounts, defaced pages, or when hardening a fresh install on shared hosting.
---

# WordPress Hardening

A defensive-security skill for diagnosing and hardening WordPress installations, with a focus on **shared-hosting environments where one compromised sub can pivot across the whole account**.

## When to invoke

Trigger this skill when any of these signals appear:

- `wp-content/uploads/**/*.php` exists (uploads should never contain PHP)
- Admin users you do not recognize, or `wp_users` entries with creation dates that don't match the site history
- `wp-config.php` modified recently with no deploy
- `mu-plugins/` contains files you did not place there
- Posts/options contain base64-encoded blobs, `eval(`, `gzinflate(`, `str_rot13(`, or hex-escape strings
- The site serves a different language/title to bots than to humans (cloaking)
- A shared-hosting account contains 1 dirty sub and N other subs — assume lateral movement until proven otherwise

## Detection — file-system indicators

Run these from the doc-root. Adjust paths for the hosting layout.

```bash
# 1. Any PHP in uploads is suspicious — production WP never writes PHP there
find wp-content/uploads -name '*.php' -o -name '*.phtml' -o -name '*.phar' 2>/dev/null

# 2. Recent PHP changes outside core/plugins/themes you control
find . -name '*.php' -mtime -30 -not -path './wp-content/cache/*' 2>/dev/null

# 3. Common webshell signatures (Sid Gifari, WSO, FilesMan, b374k, c99)
grep -rEl 'Sid[ _]Gifari|WSO [0-9]|FilesMan|c99shell|b374k|eval\(base64_decode|eval\(gzinflate|@eval\(\$_(POST|GET|REQUEST|COOKIE)' \
  --include='*.php' --include='*.phtml' . 2>/dev/null

# 4. Suspicious file names dropped by mass-compromise tools
find . \( -name 'wp-conflg.php' -o -name 'wp-info.php' -o -name 'radio.php' \
      -o -name 'about.php' -o -name 'license.php' -o -name 'lock360.php' \) 2>/dev/null

# 5. Files with execute-but-no-owner mismatch (often dropped by web user via writable dir)
find . -name '*.php' -user www-data 2>/dev/null  # adjust user for the host
```

The single highest-value query is **(1)**: a PHP file in `uploads/` is a near-certain indicator. Investigate every hit.

## Detection — database indicators

```sql
-- 1. Unexpected admin users
SELECT u.ID, u.user_login, u.user_email, u.user_registered, m.meta_value
FROM wp_users u
JOIN wp_usermeta m ON m.user_id = u.ID
WHERE m.meta_key = 'wp_capabilities' AND m.meta_value LIKE '%administrator%';

-- 2. Recently-modified options that should be static
SELECT option_name, LENGTH(option_value) AS len, option_value
FROM wp_options
WHERE option_name IN ('siteurl','home','active_plugins','template','stylesheet','admin_email','blogname')
   OR option_name LIKE 'cron%'
   OR option_name LIKE '%_transient_%spam%';

-- 3. Hidden auto-loaded options (a classic backdoor mechanism)
SELECT option_id, option_name, LENGTH(option_value) AS len
FROM wp_options
WHERE autoload = 'yes' AND LENGTH(option_value) > 50000
ORDER BY len DESC LIMIT 20;

-- 4. Posts injected with hidden links / SEO spam
SELECT ID, post_title, post_status, post_modified
FROM wp_posts
WHERE post_content LIKE '%<div style=%display:none%'
   OR post_content LIKE '%base64_decode%'
   OR post_content LIKE '%eval(%'
LIMIT 50;
```

## Containment (do this in order)

1. **Snapshot first** — full file + DB backup before touching anything. You need forensic state to learn from.
2. **Take the site offline** if possible — maintenance mode at the webserver level, not via a WP plugin (the plugin may be compromised).
3. **Rotate all credentials** treated as burned:
   - WP admin passwords (all admin accounts, then delete unknown ones)
   - DB user password (and update `wp-config.php`)
   - SFTP/SSH passwords + revoke shared keys
   - Hosting-panel password
   - API keys stored in plugins (Stripe, Mailgun, etc.)
4. **Block at the edge** — if a single attacker IP/ASN is hammering, block at Cloudflare/WAF, not just `.htaccess`.

## Cleanup

- Restore WP **core** from `wordpress.org` ZIP (do not trust `wp-admin/` and `wp-includes/` on disk).
- Restore each **plugin** from its official source. Compare hashes against fresh downloads — never just diff against another site (it may also be compromised).
- Restore each **theme** the same way. Custom themes: diff against last clean git commit.
- Wipe `wp-content/uploads/**/*.php` unconditionally.
- Drop and recreate `mu-plugins/` from a known-good source.
- Re-issue salts in `wp-config.php` ([api.wordpress.org/secret-key/1.1/salt/](https://api.wordpress.org/secret-key/1.1/salt/)) — this invalidates all existing auth cookies.

## Hardening — defense pack

Drop these into `mu-plugins/` (must-use plugins load before regular ones and cannot be disabled from the admin):

### `mu-plugins/00-disable-file-edit.php`

```php
<?php
// Block plugin/theme editing from the WP admin (a common post-compromise pivot).
define('DISALLOW_FILE_EDIT', true);
define('DISALLOW_FILE_MODS', true);
```

### `mu-plugins/01-block-php-in-uploads.php`

```php
<?php
// Belt-and-braces: also enforce at the webserver layer (.htaccess / nginx).
add_filter('upload_mimes', function ($mimes) {
    unset($mimes['php'], $mimes['phtml'], $mimes['phar']);
    return $mimes;
});
```

### `.htaccess` (Apache) — inside `wp-content/uploads/`

```apache
<FilesMatch "\.(php|phtml|phar|pl|py|cgi|asp)$">
    Require all denied
</FilesMatch>
```

### nginx (server block)

```nginx
location ~* /wp-content/uploads/.*\.(php|phtml|phar|pl|py|cgi|asp)$ {
    deny all;
    return 403;
}
```

### `mu-plugins/02-file-integrity.php`

```php
<?php
// Email alert when a PHP file under wp-content changes.
// Daily cron — adjust to match your noise tolerance.
add_action('init', function () {
    if (!wp_next_scheduled('mu_file_integrity_check')) {
        wp_schedule_event(time(), 'daily', 'mu_file_integrity_check');
    }
});
add_action('mu_file_integrity_check', function () {
    $state_file = WP_CONTENT_DIR . '/.integrity-state.json';
    $current = [];
    $iter = new RecursiveIteratorIterator(new RecursiveDirectoryIterator(WP_CONTENT_DIR));
    foreach ($iter as $f) {
        if (!$f->isFile() || $f->getExtension() !== 'php') continue;
        if (strpos($f->getPathname(), '/cache/') !== false) continue;
        $current[$f->getPathname()] = hash_file('sha256', $f->getPathname());
    }
    if (file_exists($state_file)) {
        $prior = json_decode(file_get_contents($state_file), true);
        $diff = array_diff_assoc($current, $prior) + array_diff_key($current, $prior) + array_diff_key($prior, $current);
        if (!empty($diff)) {
            wp_mail(get_option('admin_email'),
                '[INTEGRITY] PHP file changes on ' . home_url(),
                "Changed/new/removed PHP files:\n\n" . print_r(array_keys($diff), true));
        }
    }
    file_put_contents($state_file, json_encode($current));
});
```

## Shared-hosting pivot — investigate every sub

If one sub on a shared account is compromised, **assume the others are too** until proven clean. Walk every doc-root on the account and re-run the detection queries. Often the same attacker drops the same shell with slight name variations across all sites under the panel user.

## What this skill will not do

- It does not exploit, brute-force, or remove protections from sites you do not own.
- It does not recommend disabling security headers, WAFs, or auth for any reason.
- It assumes you have explicit authorization for the target site.

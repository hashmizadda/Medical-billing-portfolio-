# Muhammad Hafeez — Medical Billing & RCM Portfolio

## Requirements
- PHP 8.0+ (PHP 8.1+ recommended)
- Apache/Nginx hosting with PHP enabled
- PHP `mail()` configured, or replace the mail handler with authenticated SMTP

## Run locally
1. Install PHP.
2. From this project folder run: `php -S localhost:8000`
3. Open `http://localhost:8000`

## Personalize before publishing
1. Your supplied portrait is already installed at `assets/images/muhammad-hafeez.jpg` and connected to the home page. Replace it only if you want to use a different photo.
2. Open `includes/data.php` and replace every social link with your actual profile URL.
3. Review the About page and experience wording. Confirm every platform and skill accurately reflects your experience.
4. Verify the email address and WhatsApp number in `index.php`, `includes/data.php` and `send-message.php`.
5. Upload the folder to PHP-enabled hosting and enable HTTPS.

## Contact form
The form posts to `send-message.php`, which uses PHP `mail()`. Many hosts disable or restrict `mail()`. For reliable delivery, configure SMTP through a reputable provider and a maintained mail library such as PHPMailer. Never put an email password or SMTP secret in public JavaScript or commit it to a public repository.

## Why this uses PHP, HTML5 and JavaScript
- HTML5: semantic pages and accessible form structure.
- PHP: page routing, reusable content data and server-side form validation.
- JavaScript: responsive navigation and submission feedback.
- Python: `tools/generate_specialty_pages.py` is an optional content utility for exporting the specialty catalogue as JSON; Python is not required to run the website.

## Important
This is a professional portfolio starter, not a production medical billing platform. Do not collect patient protected health information (PHI) through this public contact form. Do not upload patient records or other sensitive healthcare data.

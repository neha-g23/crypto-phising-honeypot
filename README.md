# crypto-phising-honeypot
A simulated phishing site to demonstrate how fake wallets steal crypto.

Fake MetaMask Login
A simulated phishing site to demonstrate how fake wallets steal crypto.

How it works
The front-end is a cloned login page (HTML) based on the real MetaMask design

The back-end is a Python Flask app that:

- Accepts input from the fake login or recovery form

- Logs fake credentials to a honeypot.log file

- Redirects to a fake error page that looks believable

Features
- UI mimicking the real MetaMask Card login

- "Forgot password" buttons (redirects to another page where promted to enter seed phrase)

Fake seed phrase submission form

Honeypot routes like /private.key, /admin, and /.env that log access attempts

Every login attempt always fails with a fake error message
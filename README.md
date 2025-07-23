# Secure Login System – Cybersecurity Edition

A modern, secure Django login system with advanced security features and a cyber-themed UI.

## Features
- **Custom User Model** with bcrypt password hashing
- **IP blocking** after 3 failed login attempts
- **VPN/Proxy detection** (IPQualityScore API)
- **Email alerts** on failed logins
- **Logging** of login attempts
- **Cybersecurity-themed UI** (dark, neon, modern)
- **Django messages** for all errors/blocks, styled in the login box

## Screenshots
![Login UI](screenshots/login.png)

## Quick Start
1. **Clone the repo:**
   ```sh
   git clone https://github.com/Dynopllot/Secure-login-system.git
   cd Secure-login-system
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run migrations:**
   ```sh
   python manage.py migrate
   ```
4. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```
5. **Run the server:**
   ```sh
   python manage.py runserver
   ```

## Configuration
- Set your email and IPQualityScore API key in `settings.py`.
- To disable VPN/proxy blocking for local dev, set `VPN_PROXY_BLOCK_ENABLED = False` in `settings.py`.

## Security Notes
- For local development, VPN/proxy detection may block localhost. Adjust as needed.
- All error/block messages are shown in the cyber-themed login box.

## License
MIT
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

## Usage
- Visit `http://127.0.0.1:8000/accounts/login/` to log in.
- Register a new user or log in with your superuser credentials.
- After 3 failed login attempts from the same IP, that IP will be blocked.
- If VPN/Proxy is detected (using IPQualityScore), login is blocked and a message is shown.
- All failed logins are logged to `logs/login_attempts.log`.
- Email alerts are sent on failed logins (configure your email in `settings.py`).

## API Integration (IPQualityScore)
- The system uses the [IPQualityScore IP Reputation API](https://www.ipqualityscore.com/documentation/proxy-detection/overview) to detect VPN/proxy usage.
- Set your API key in `settings.py`:
  ```python
  IPQUALITYSCORE_API_KEY = 'your_api_key_here'
  ```
- The API is called in `accounts/views.py`:
  ```python
  resp = requests.get(f'https://ipqualityscore.com/api/json/ip/{API_KEY}/{ip}', timeout=5)
  data = resp.json()
  if data.get('proxy'):
      # Block login
  ```
- For local development, you may want to skip proxy checks for `127.0.0.1`.

## Configuration
- Set your email and IPQualityScore API key in `settings.py`.
- To disable VPN/proxy blocking for local dev, set `VPN_PROXY_BLOCK_ENABLED = False` in `settings.py`.

## Security Notes
- For local development, VPN/proxy detection may block localhost. Adjust as needed.
- All error/block messages are shown in the cyber-themed login box.

## License
MIT
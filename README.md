# Secure Login System – Cybersecurity Edition

## Objective
To design and develop a robust, secure login system using Django and Python that ensures user authentication through encrypted password storage (bcrypt), detects suspicious access patterns (including VPN usage), blocks IP addresses after multiple failed attempts, and sends real-time email alerts to administrators. The system integrates logging mechanisms to track login activity and includes a web-based admin dashboard for viewing and managing authentication logs. The primary objective is to enhance login security, prevent brute-force attacks, and provide a scalable framework for real-world web applications.

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (custom cyber-themed styling)
- **Database:** SQLite (default, can be swapped)
- **Security:** bcrypt, IPQualityScore API, Django messages

## Features
- Custom user model with bcrypt password hashing
- IP blocking after 3 failed login attempts
- VPN/Proxy detection (IPQualityScore API)
- Email alerts on failed logins
- Logging of login attempts
  
## How It Works
1. **User Registration & Login:**
   - Users register and log in using a custom user model.
   - Passwords are hashed with bcrypt for strong security.
2. **Login Security:**
   - All login attempts are logged.
   - After 3 failed attempts from the same IP, that IP is temporarily blocked.
   - If a VPN/proxy is detected (via IPQualityScore), login is blocked and a warning is shown.
3. **Alerts & Monitoring:**
   - Failed logins trigger email alerts to the admin/user.
   - All events are logged for audit and monitoring.
4. **User Experience:**
   - All error and block messages are shown in a login box.
   - Dashboard displays security features and tips after login.

## Screenshots

### 1. Login Page

<img width="1280" height="694" alt="image" src="https://github.com/user-attachments/assets/645f594c-f8ad-4b45-a6eb-5a31455fb62c" />


### 2. Register Page
 
<img width="1280" height="791" alt="image" src="https://github.com/user-attachments/assets/31536925-d96a-456a-8d42-f7472b7274bd" />

### 3. Cybersecurity Dashboard
 
<img width="1280" height="895" alt="image" src="https://github.com/user-attachments/assets/c34ff4d4-5b55-4d97-819b-979b4cf8b172" />

### 4. IP Blocked Message

 <img width="1280" height="531" alt="image" src="https://github.com/user-attachments/assets/27172fb6-6045-4fe7-9cea-2b4de83cf573" />


### 5. VPN/Proxy Blocked Message

 <img width="1280" height="676" alt="image" src="https://github.com/user-attachments/assets/b0d0db77-f80f-4dfd-b1ea-6e179592fa9a" />


### 6. Email Alert Example

<img width="1167" height="572" alt="image" src="https://github.com/user-attachments/assets/c0784f54-45da-4f59-abbb-2f7b377a1273" />

### 7. Admin Dashboard

<img width="1280" height="515" alt="image" src="https://github.com/user-attachments/assets/9384b953-3852-4b5a-ab61-18e694a180f4" />

<img width="1280" height="631" alt="image" src="https://github.com/user-attachments/assets/a2ea19b6-9981-4de5-986a-f04d23d353fe" />

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
- All error/block messages are shown in the login box.

## License
MIT

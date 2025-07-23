from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, LoginForm
from django.contrib import messages
import logging
from django.core.mail import send_mail
from django.conf import settings
import requests

logger = logging.getLogger('django')
FAILED_LOGINS = {}

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    from django.contrib.auth import authenticate
    ip = get_client_ip(request)
    # Block all VPN/Proxy logins immediately if enabled in settings
    if getattr(settings, 'VPN_PROXY_BLOCK_ENABLED', True) and is_proxy_ip(ip):
        messages.error(request, 'Login from VPN/Proxy is not allowed.')
        logger.warning(f"Blocked login attempt from VPN/Proxy IP: {ip}")
        return render(request, 'accounts/login.html', {'form': LoginForm()})
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"Successful login: {user.username} from IP {ip}")
            FAILED_LOGINS[ip] = 0
            return redirect('home')
        else:
            FAILED_LOGINS[ip] = FAILED_LOGINS.get(ip, 0) + 1
            logger.warning(f"Failed login attempt from IP {ip}")
            messages.error(request, 'Please enter the correct password.')
            send_alert_email(ip)
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def is_proxy_ip(ip):
    API_KEY = '4gpW491Gyj0WEzTsTYgfMRrVfJN7dMtX'
    try:
        resp = requests.get(f'https://ipqualityscore.com/api/json/ip/{API_KEY}/{ip}', timeout=5)
        data = resp.json()
        logger.info(f"IPQualityScore response for {ip}: {data}")  # Debug log
        # Only block if 'proxy' is True (less strict, fewer false positives)
        if data.get('proxy'):
            return True
        return False
    except Exception as e:
        logger.error(f"IPQualityScore API error: {e}")
        return False

def home_view(request):
    return render(request, 'accounts/home.html')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

def send_alert_email(ip):
    recipient = getattr(settings, 'ALERT_EMAIL_RECIPIENT', settings.EMAIL_HOST_USER)
    send_mail(
        subject='[Alert] Failed Login Attempt',
        message=f'Failed login attempt detected from IP: {ip}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient],
        fail_silently=True,
    )

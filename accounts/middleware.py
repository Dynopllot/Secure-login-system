

from django.shortcuts import render
from .views import FAILED_LOGINS

class IPBlockerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if FAILED_LOGINS.get(ip, 0) >= 3:
            from django.contrib import messages
            from .forms import LoginForm
            messages.error(request, "IP blocking after 3 failed attempts: Your IP has been temporarily blocked for security reasons. Please try again later or contact support if you believe this is a mistake.")
            return render(request, 'accounts/login.html', {'form': LoginForm()})
        return self.get_response(request)

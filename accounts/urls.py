
from django.urls import path
from .views import register_view, login_view, home_view
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', home_view, name='home'),
]

from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import LogInForm

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LogInForm), name='login'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout, name='logout'),
]

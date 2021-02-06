from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# Account's URLs
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

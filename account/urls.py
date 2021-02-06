from django.urls import path
from . import views


# Account's URLs
urlpatterns = [
    path('register/', views.register, name='register'),
]

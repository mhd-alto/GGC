from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_thread, name='addthread'),
    path('', views.thread, name='thread')
]

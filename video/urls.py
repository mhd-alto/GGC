from django.urls import path
from . import views
# Account's URLs
urlpatterns = [
      path('', views.video, name='video'),
      path('add/', views.add_video, name='videoadd'),
   ]

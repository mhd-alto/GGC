from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_thread, name='addthread'),
    path('edit/<int:thread_id>/', views.edit_thread, name='thread_edit'),
    path('', views.thread, name='thread')
]

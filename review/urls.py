from django.urls import path
from . import views


# Review's URLs
urlpatterns = [
    path('', views.reviews_list, name='review'),
    path('add/', views.add_review, name='addreview'),
]

from django.urls import path
from . import views


# Trade's urls
urlpatterns = [
    path('', views.trade_page, name='trade_page'),
    path('add/', views.add_in_trade, name='add_in_trade'),
]

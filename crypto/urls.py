from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prices/', views.prices, name='prices'),
    path('all_prices/', views.all_prices, name='all_prices')
]

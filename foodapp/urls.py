# foodapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<int:restaurant_id>/', views.menu_item_list, name='menu_item_list'),
    path('register/', views.register, name='register'),
]

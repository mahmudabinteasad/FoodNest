# foodapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:restaurant_id>/', views.menu_item_list, name='menu_item_list'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login_view, name='login'),  # using custom login function-based view
]

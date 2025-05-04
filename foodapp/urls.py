# foodapp/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:restaurant_id>/', views.menu_item_list, name='menu_item_list'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('restaurants/', views.show_restaurants, name='restaurants'),
]

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView  # ✅ ADD THIS LINE

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:restaurant_id>/', views.menu_item_list, name='menu_item_list'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login_view, name='login'),  # using custom login function-based view
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # ✅ Now it will work
    path('restaurants/', views.show_restaurants, name='restaurants'),
]

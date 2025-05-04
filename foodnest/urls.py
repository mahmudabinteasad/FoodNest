# foodnest/urls.py

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foodapp.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='foodapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='foodapp/logout.html'), name='logout'),
]

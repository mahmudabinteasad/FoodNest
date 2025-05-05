# foodapp/views.py

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.db import connection
from django.contrib.auth.hashers import make_password
from .models import Restaurant, MenuItem
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def home(request):
    restaurants = Restaurant.objects.all()
    featured_restaurants = Restaurant.objects.filter(is_featured=True)[:5]
    paginator = Paginator(restaurants, 20)
    first_page_restaurants = paginator.get_page(1)
    return render(request, 'home.html', {
        'restaurants': first_page_restaurants,
        'featured_restaurants': featured_restaurants,
    })

def restaurant_list(request):
    page_number = request.GET.get('page')
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 6)
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('restaurant_card_partial.html', {'restaurants': page_obj})
        return JsonResponse({'html': html})

    return render(request, 'restaurant_list.html', {'restaurants': page_obj})

def menu_item_list(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    return render(request, 'menu_item_list.html', {'restaurant': restaurant, 'menu_items': menu_items})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            # Get data
            username = user.username
            email = user.email
            phone = form.cleaned_data.get('phone_number')
            password_raw = form.cleaned_data.get('password1')
            hashed_password = make_password(password_raw)
            address = form.cleaned_data.get('address')

            # Insert into custom users table using raw SQL
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO users (username, password, email, phone, address)
                    VALUES (%s, %s, %s, %s, %s)
                """, [username, hashed_password, email, phone, address])

            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def custom_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        users = User.objects.filter(email=email)
        if users.exists():
            user = users.first()  # Use the first user with this email
            user = authenticate(username=user.username, password=password)
            if user:
                auth_login(request, user)
                return redirect('home')

        return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def cart(request):
    return render(request, 'cart.html')

def show_restaurants(request):
    return render(request, 'restaurants.html')

def update_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # Future: Update raw SQL here if needed
        return redirect('some_page')
    return render(request, 'update_profile.html')

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .models import Restaurant, MenuItem
from .forms import CustomUserCreationForm  # your custom form with email, phone, username, password
from django.contrib.auth.decorators import login_required

def home(request):
    restaurants = Restaurant.objects.all()
    featured_restaurants = Restaurant.objects.filter(is_featured=True)[:4]
    paginator = Paginator(restaurants, 6)
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
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# ✅ Login with email and password
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
        
        # Optional: you can show an error message here
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

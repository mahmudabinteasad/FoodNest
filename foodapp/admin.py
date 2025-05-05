# foodapp/admin.py

from django.contrib import admin
from .models import Restaurant, MenuItem, Order, OrderDetail

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'address', 'phone')
    list_filter = ('is_featured',)
    search_fields = ('name', 'address')
    
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderDetail)
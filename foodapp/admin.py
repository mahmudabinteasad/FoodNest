# foodapp/admin.py

from django.contrib import admin
from .models import Restaurant, MenuItem, Order, OrderDetail

admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderDetail)

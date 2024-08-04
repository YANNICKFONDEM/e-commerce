from django.contrib import admin
from .models import Customer, Tag, product,Order 
# Register your models here.

admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(product)
admin.site.register(Order)
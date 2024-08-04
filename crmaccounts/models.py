from django.db import models
from django.contrib.auth.models import User
from item.models import Item
# Create your models here.


class Customer(models.Model):
    user = models.ManyToManyField(User, related_name='customer')
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name =models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
        
class product(models.Model):
    
    name = models.ForeignKey(Item, on_delete=models.CASCADE)
    # price = models.FloatField(null=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # description = models.CharField(max_length=100, null=True)
    # date_created = models.DateTimeField(auto_now_add=True)
    # tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return str(self.name)
    
class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Out for delivery', 'Out for delivery'),
            ('Delivered', 'Delivered'),
            )
        
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return str(self.product.name)


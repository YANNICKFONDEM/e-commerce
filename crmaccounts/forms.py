from django.forms import ModelForm

from .models import Order, Customer

class OrdeForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
class CreateCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name','phone','email']
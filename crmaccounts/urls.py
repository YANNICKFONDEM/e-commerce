from django.urls import path
from . import views


app_name='crmaccounts'
urlpatterns = [
    path('crmhome/',views.home, name='crmhome'),
    path('crmcustomer/<int:pk>',views.customer, name='crmcustomer'),
    
    path('createcustomer/',views.createcustomer,name='createcustomer'),
    path('deletecustomer/<int:pk>',views.deletecustomer, name='deletecustomer'),
    
    path('product/',views.product, name='product'),
    path('create_order/<int:pk>',views.createOrder, name='create_order'),
    path('update_order/<int:pk>',views.updateOrder, name='update_order'),
    path('delete_order/<int:pk>',views.deleteOrder, name='delete_order'),
]

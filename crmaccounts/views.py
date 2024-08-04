from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django .contrib import messages
from item.models import Item
from .models import Order, Customer
from . forms import OrdeForm, CreateCustomerForm
from coreApp.decorators import allowed_users, admin_only
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
@allowed_users(allowed_roles=['admin'])
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()
    
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()
    
    context = {'orders':orders, 'customers':customers,'total_customers':total_customers,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request, 'crmaccounts/crmhome.html',context)


@login_required
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customers = Customer.objects.get(pk=pk)
    
    orders = customers.order_set.all()
    order_count = orders.count()
    
    context = {'customers':customers, 'orders':orders, 'order_count':order_count}
    return render(request, 'crmaccounts/crmcustomers.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def createcustomer(request):
    customers = Customer.objects.all()
    form = CreateCustomerForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            messages.success(request, f"customer created successfully ✅.")
            form.save()
            return redirect('crmaccounts:crmhome')
        else:
            form=CreateCustomerForm()
    context={'customers':customers,'form':form}
    return render(request, 'crmaccounts/createcustomer.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def deletecustomer(request, pk):
    customers = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        customers.delete()
        messages.info(request,f"customer deleted successfully❗")
        return redirect('crmaccounts:crmhome')
    context = {'customers':customers}
    return render(request, 'crmaccounts/deletecustomer.html',context)
    
def product(request):
    products = Item.objects.all()[0:8]
    context = {'products':products}
    
    return render(request, 'crmaccounts/product.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customers = Customer.objects.get(pk=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customers)
    # form = OrdeForm(initial={'customer':customers})
    if request.method == 'POST':
        # form = OrdeForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customers)
        if formset.is_valid():
            messages.success(request, f"Order created successfully ✅.")
            formset.save()
            return redirect('crmaccounts:crmhome')
        
    context = {'formset':formset}
    
    return render(request, 'crmaccounts/order_form.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(pk=pk)
    form = OrdeForm(instance=order)
    if request.method == 'POST':
        form = OrdeForm(request.POST, instance=order)
        if form.is_valid():
            messages.info(request, f"Order updated successfully✅")
            form.save()
            return redirect('crmaccounts:crmhome')
        
    context = {'formset':form}
    return render(request, 'crmaccounts/order_form.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        
        order.delete()
        messages.info(request, f"order deleted successfully❗")
        return redirect('crmaccounts:crmhome')
    context = {'item':order}
    
    return render(request, 'crmaccounts/delete.html',context)
from django.shortcuts import render, redirect

from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.contrib import messages
from item.models import Category, Item
from .forms import SignupForm

from .decorators import allowed_users, admin_only


# Create your views here.


# @allowed_users(allowed_roles=['admin'])

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {'items':items,'categories':categories}
    return render(request, 'coreApp/index.html',context)

def contact(request):
    return render(request, 'coreApp/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.info(request, 'your account has been created successful')
            
            return redirect('/login/')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('/signup/')
    else:
        
        form = SignupForm()
    
    
    return render(request, 'coreApp/signup.html',{'form':form})


def logoutpage(request):
    logout( request)
    return redirect('coreApp:index')
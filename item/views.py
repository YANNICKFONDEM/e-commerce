from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from coreApp.decorators import allowed_users
from .form import LocationForm
from .forms import NewItemForm, EditItemForm
from .models import Category, Item, City

from django.views.generic import DetailView
from History.mixins import ObjectViewMixin
from History.signals import object_viewed_signal

def items(request,):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    city = City.objects.all()
    
    if category_id:
        items=items.filter(category_id=category_id)
    
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
        
    # Assume you want to track each individual item detail view
    if items.exists() and request.user.is_authenticated:
        for item in items:
            object_viewed_signal.send(
                sender=item.__class__,
                instance=item,
                request=request
            )
    
    return render(request, 'item/items.html', {'items':items, 'query':query, 'categories':categories, 'city':city, 'category_id': int(category_id)})

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    
     # Send signal to track the item view
    object_viewed_signal.send(
        sender=item.__class__,
        instance=item,
        request=request
    )
    
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:6]
    
    return render(request, 'item/detail.html',{'item':item,'related_items': related_items})

# def Location(request):
#     if request.method == 'POST':
#         form = LocationForm(request.POST, request.FILES)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.created_by = request.user
#             item.save()
            
#             return redirect('item:detail', pk=item.id)
#     else:
        
#         form = LocationForm()
    
    
#     return render(request, 'coreApp/base.html',{'form':form, 'title':'New item'})

@login_required
@allowed_users(allowed_roles=['admin'])
def New(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            return redirect('item:detail', pk=item.id)
    else:
        
        form = NewItemForm()
    
    
    return render(request, 'item/form.html',{'form':form, 'title':'New item'})

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            form.save()
            
            return redirect('item:detail', pk=item.id)
    else:
        
        form = EditItemForm(instance=item)
    
    
    return render(request, 'item/form.html',{'form':form, 'title':'Edit item'})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')

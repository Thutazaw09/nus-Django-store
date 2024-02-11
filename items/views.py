from django.shortcuts import render,get_object_or_404,redirect
from .models import Item
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .form import NewItemForm
# Create your views here.
def detail(request:HttpRequest, pk:int):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    
    
    return render(
        request,'items/detail.html',{
            'item':item,
            'related_item':related_items
        }
    )
    
@login_required 
def newItem(request:HttpRequest):
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('items:store-detail',pk=item.id)
    else:
        form = NewItemForm()
        
        
    return render(request,'items/form.html',{
        'form':form,
        'title': "New Item",
    })
    
    

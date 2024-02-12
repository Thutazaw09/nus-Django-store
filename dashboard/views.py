from django.shortcuts import render,get_object_or_404
from items.models import Item
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest


@login_required
def index(request:HttpRequest):
    items = Item.objects.filter(created_by=request.user)
    
    return render(request,'dashboard/index.html',{
        'items': items
    })
    
    

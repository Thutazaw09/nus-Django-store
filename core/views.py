from django.shortcuts import render,redirect
from django.http import HttpRequest
from items.models import Category,Item
from .form import SignupForm

def index(request:HttpRequest):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request,'core/index.html',{
        'catogories':categories,
        'items':items
    })

def contact(request:HttpRequest):
    return render(request,'core/contact.html')

def about(request:HttpRequest):
    return render(request,'core/about.html')

def term_of_use(request:HttpRequest):
    return render(request,'core/term_of_use.html')

def privacy_and_policy(request:HttpRequest):
    return render(request,'core/privacy_and_policy.html')
 
def signup(request:HttpRequest):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('core:store-login')
       
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
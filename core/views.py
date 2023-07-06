from django.shortcuts import render, redirect
from django.db.models import Count
from item.models import Item, Category
from .models import Banner
from .forms import SignUpForm

from django.contrib.auth import logout as logout_function

def index(request):
    newest_items = Item.objects.filter(is_sold=False)[0:6]
    top_viewed_items = Item.objects.all().order_by('-viewed')[:6]
    categories = Category.objects.annotate(item_count=Count('items')).order_by('-item_count')[:6]
    banners = Banner.objects.all()
    context = {
        'categories': categories,
        'newest_items': newest_items,
        'top_viewed_items': top_viewed_items,
        'banners': banners
    }
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'core/signup.html', context)

def logout(request):
    logout_function(request)
    return redirect('/')
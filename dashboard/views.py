from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from core.models import Profile
from item.models import Item

@login_required
def index(request):
    profile = get_object_or_404(Profile, user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def items(request):
    items = Item.objects.filter(created_by=request.user)
    context = {
        'items': items
    }
    return render(request, 'dashboard/items.html', context)
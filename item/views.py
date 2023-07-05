from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from.forms import NewItemForm, EditItemForm

from .models import Item, Category

def items(request):
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    if category_id != 0:
        items = items.filter(category=category_id)
    if query is not None:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context = {
        'items': items,
        'query': query,
        'category_id': category_id,
        'categories': categories
    }
    return render(request, 'item/items.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:10]
    context = {
        'item': item,
        'related_items': related_items
    }
    return render(request, 'item/detail.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    context = {'form': form}
    return render(request, 'item/new.html', context)

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
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'item/edit.html', context)

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:dashboard')
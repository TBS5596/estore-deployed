from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Cart, Order
from item.models import Item

from .forms import AddToCartForm, AddToOrderForm

@login_required
def index(request):
    cart_items = Cart.objects.filter(user=request.user).filter(is_ordered=False)
    context = {
        'cart_items': cart_items
    }
    return render(request, 'cart/index.html', context)

@login_required
def add(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            cart_item = Cart.objects.create(item=Item, user=request.user, quantity=form.cleaned_data['quantity'])
            print(f'before calc @s {cart_item.id} {cart_item.item_id} {cart_item.quantity} {cart_item.total_price}')
            cart_item.cal_total()
            print(f'after calc @s {cart_item.id} {cart_item.item_id} {cart_item.quantity} {cart_item.total_price}')
            cart_item.save()
            print(f'saved @s {cart_item.id} {cart_item.item_id} {cart_item.quantity} {cart_item.total_price}')
            return redirect('cart:cart', pk=pk)
    return redirect('item:detail', pk=pk)

@login_required
def edit(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    if request.method == 'POST':
        form = AddToCartForm(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            return redirect('cart:cart')
    else:
        form = AddToCartForm(instance=cart_item)
    context = {
        'form':form,
        'cart_item':cart_item
    }
    return render(request, 'cart/edit.html', context)

@login_required
def delete(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    if cart.user == request.user:
        cart.delete()
    return redirect('cart:cart')

@login_required
def add_to_orders(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    if request.method == 'POST':
        form = AddToOrderForm(request.POST)
        if form.is_valid():
            form.save()
            cart.is_ordered = True
            cart.save()
            return redirect('cart:orders')
    else:
        form = AddToOrderForm()
    context = {
        'form': form,
        'cart_item': cart_item
    }
    return render(request, 'cart/orders.html', context)

@login_required
def orders(request):
    orders = Order.objects.filter(cart__user=request.user)
    context = {'orders': orders}
    return render(request, 'cart/orders.html', context)
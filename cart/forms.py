from django import forms

from .models import Cart, Order

class AddToCartForm(forms.ModelForm):
    class Meta:
        model =  Cart
        fields = ('quantity',)

class AddToOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('additional_info',)
from django import forms

from .models import Cart, Order

class AddToOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('additional_info',)
from django import forms
from order.models import ShopCart, Order


class ShopCartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity', 'color', 'size', ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'zip_code', 'country', 'city', 'feedback', ]

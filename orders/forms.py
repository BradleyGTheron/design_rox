from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','address','postal_code','city','provice','delivery_method','delivery_method_confirmation']

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['postal_code'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['provice'].widget.attrs['class'] = 'form-control'
        self.fields['delivery_method'].widget.attrs['class'] = 'form-control'
        self.fields['delivery_method_confirmation'].label = ''
        self.fields['delivery_method_confirmation'].widget.attrs['class'] = 'form-check-input'
        self.fields['delivery_method_confirmation'].help_text = '<span>Please confirm that the corect delivery method has been selected.</span>'

from django import forms

PRINT_QUANITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddPrintForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRINT_QUANITY_CHOICES,
                                        coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

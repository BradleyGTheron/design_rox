from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from print.models import Print
from .cart import Cart
from .forms import CartAddPrintForm

@require_POST
def cart_add(request, print_id):
    cart = Cart(request)
    print = get_object_or_404(Print, id=print_id)
    form = CartAddPrintForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(print=print,
                quantity=cd['quantity'],
                update_quantity=cd['update'])
        return redirect('cart:cart_detail')


def cart_remove(request, print_id):
    cart = Cart(request)
    print = get_object_or_404(Print, id=print_id)
    cart.remove(print)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddPrintForm(initial={'quantity': item['quantity'],
                                                        'update': True})

    return render(request, 'cart/detail.html', {'cart': cart})

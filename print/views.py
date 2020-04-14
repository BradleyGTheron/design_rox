from django.shortcuts import render, get_object_or_404
from .models import Category, Print, Gallery
from cart.forms import CartAddPrintForm

def home(request):
    sale_prints = Print.objects.filter(home_page = True, promotion = 'SAL')
    kids_prints = Print.objects.filter(home_page = True, category = 1)
    gallery_prints = Gallery.objects.filter(enable = True)
    return render(request, 'print/home.html', {'sale_prints': sale_prints,
                                                'kids_prints': kids_prints,
                                                'gallery_prints': gallery_prints })


def print_detail(request, id, slug):
    print = get_object_or_404(Print, id=id, slug=slug, enable=True)
    cart_print_form = CartAddPrintForm()
    return render(request, 'print/print_detail.html', {'print': print,
                                                    'cart_print_form': cart_print_form})

from django.shortcuts import render, get_object_or_404
from .models import Category, Print

def home(request):
    sale_prints = Print.objects.filter(home_page = True)
    return render(request, 'print/home.html', {'sale_prints': sale_prints})

# def print_list(request, category_slug = None):
#     category = None
#     categories = Category.objects.all()
#     prints = Print.objects.filter(enable=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products =products.filter(category=category)
#         return render(request, 'print/print/list.html', {'category': category,
#                                                         'categories': categories,
#                                                         'prints': prints})

# def print_details(request, id, slug):
#     print = get_object_or_404(Print, id=id, slug=slug, enabled=True)
#     return render(request,
#                     'print/print/details.html',
#                     {'print': print,
#                     'cart_print_form': cart_print_form})

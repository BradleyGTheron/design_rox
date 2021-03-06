from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method=='POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        print=item['print'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clears the Cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})

# Create your views here.

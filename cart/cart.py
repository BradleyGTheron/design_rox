from decimal import Decimal
from django.conf import settings
from print.models import Print

class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the sessions
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the prints from the databases
        """
        print_ids = self.cart.keys()
        # get the print object and add them to the cart
        prints = Print.objects.filter(id__in=print_ids)
        for print in prints:
            self.cart[str(print.id)]['print'] = print

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all the items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())


    def add(self, print, quantity, update_quantity=False):
        """
        Add a product to the cart or update its quantity
        """
        print_id = str(print.id)
        if print_id not in self.cart:
            self.cart[print_id] = {'quantity':0,
                                    'price': str(print.discounted_price)}

        if update_quantity:
            self.cart[print_id]['quantity'] = quantity
        else:
            self.cart[print_id]['quantity'] += quantity
        self.save()

    def remove(self, print):
        """
        Remove a product from the cart
        """
        print_id = str(print.id)
        if print_id in self.cart:
            del self.cart[print_id]
            self.save()

    def save(self):
        # update the session Cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as 'modified' to make sure it is saved
        self.session.modified = True

    def clear(self):
        #empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

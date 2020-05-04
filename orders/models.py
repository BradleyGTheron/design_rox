from django.db import models
from print.models import Print

class Order(models.Model):
    COLLECTION = 'COL'
    COURIER = 'COR'
    DROPOFF = 'DRP'

    EASTERN_CAPE = 'EC'
    FREE_STATE = 'FS'
    GAUTENG = 'GT'
    KWAZULU_NATAL = 'NL'
    LIMPOPO = 'LP'
    MPUMALANGA = 'MP'
    NORTHERN_CAPE = 'NC'
    NORTH_WEST = 'NW'
    WESTERN_CAPE = 'WC'

    DELIVERY_METH0D = [
        (COLLECTION, 'Collect'),
        (COURIER, 'Courrier'),
        (DROPOFF, 'Drop Off'),
    ]

    PROVINCE = [
        (EASTERN_CAPE, 'Eastern Cape'),
        (FREE_STATE, 'Free State'),
        (GAUTENG, 'Gauteng'),
        (KWAZULU_NATAL, 'Kwazulu Natal'),
        (LIMPOPO, 'Limpopo'),
        (MPUMALANGA, 'Mpumalanga'),
        (NORTHERN_CAPE, 'Northern Cape'),
        (NORTH_WEST, 'Norht West'),
        (WESTERN_CAPE, 'Western Cape'),
    ]

    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('email')
    address = models.CharField('Street Address', max_length=200, blank=True)
    suburb = models.CharField('Suburb', max_length=50, blank=True)
    postal_code = models.CharField('Postal Code', max_length=5, blank=True)
    city = models.CharField('City', max_length=50, blank=True)
    provice = models.CharField('Province',max_length=2,choices=PROVINCE,default=WESTERN_CAPE, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField('Paid', default=False)
    delivery_method = models.CharField('Delivery Method', max_length=3, choices=DELIVERY_METH0D,default=COLLECTION, blank=True)
    delivery_method_confirmation = models.BooleanField('Delivery Method Confirmation',default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete = models.CASCADE)
    print = models.ForeignKey(Print, related_name='order_items', on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

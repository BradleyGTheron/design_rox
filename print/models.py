from django.db import models
from django.urls import reverse

# --------- CATEGORY MODEL --------------

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Print Category'
        verbose_name_plural = 'Print Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('print:product_list_by_category', args=[self.slug])

# ---------- PRINT MODEL --------------------

class Print(models.Model):
    GLOSS = 'GLS'
    MATT = 'MAT'
    FEATURED = 'FEA'
    SPECIALS = 'SPE'
    SALE = 'SAL'
    NONE = 'NAN'
    A3 = 'A3'
    A4 = 'A4'
    A5 = 'A5'

    FINISH_CHOICES = [
        (GLOSS, 'Gloss'),
        (MATT, 'Matt'),
    ]

    PROMOION_CHOICES = [
        (FEATURED,'Featured'),
        (SPECIALS, 'Specials'),
        (SALE, 'Sale'),
        (NONE,'None'),
    ]

    SIZE = [
        (A3, 'A3'),
        (A4, 'A4'),
        (A5, 'A5'),
    ]

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    print_code = models.CharField('Print Code',max_length=20, db_index=True)
    name = models.CharField('Print Name', max_length=100)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField('Print Description', null=True, blank=True)
    frame = models.BooleanField('Print Framed')
    size = models.CharField('Print Size',max_length=3,choices=SIZE,default=A4)
    finish = models.CharField('Print Finish',max_length=3,choices=FINISH_CHOICES,default=GLOSS)
    price = models.DecimalField('Selling Price (R)',max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField('Discount (%)',default=0)
    image = models.ImageField('Main Image',upload_to='prints/', blank=True)
    image_tn = models.ImageField('Thumbnail Image',upload_to='prints/',blank=True)
    promotion = models.CharField('Print Promotion Status',max_length=3,choices=PROMOION_CHOICES,default=NONE)
    home_page = models.BooleanField(default=False)
    enable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-category',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('print:product_detail', args=[self.id, self.slug])

    @property
    def discounted_price(self):
        selling = self.price - (self.price * self.discount/100)
        return selling

# ----------- GALERY MODEL (Gallery Images on the home page) -------------------------

class Gallery(models.Model):
    image = models.ImageField('Main Image',upload_to='prints/', blank=True)
    image_tn = models.ImageField('Thumbnail Image',upload_to='prints/',blank=True)
    name = models.CharField('Print Title', max_length=100)
    sub_title = models.CharField('Sub Title', max_length=30)
    description = models.TextField('Print Description', null=True, blank=True)
    print_right = models.BooleanField(default=True)
    enable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Home Gallery Image'
        verbose_name_plural = 'Home Gallery Images'

    def __str__(self):
        return self.name

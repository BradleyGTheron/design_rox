from django.contrib import admin
from .models import Category, Print

class CategoryAdmin(admin.ModelAdmin):
    list_display =['name','slug']
    prepopulated_fields = {'slug':('name',)}

class PrintAdmin(admin.ModelAdmin):
    list_display = ['print_code','image', 'name','price', 'discount','discounted_price','category','promotion','home_page','enable']
    list_filter = ['category','promotion','home_page','enable']
    list_editable = ['price','discount','promotion','home_page','enable']
    ordering = ['name']
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name','print_code']
    list_per_page = 20
    actions = ('set_print_to_sale','set_print_to_feature','set_print_to_special','set_print_to_none',
                'set_print_to_disabled','set_print_to_enabled')

    fields = ('category','print_code','name','slug','description',('size','finish'),'frame',('price','discount'),('image','image_tn'),('promotion','home_page'),'enable')

# SETS THE SELECTED PRINTS PROMOTION STATUS TO SALE

    def set_print_to_sale(self, request, queryset):
        count = queryset.update(promotion='SAL')
        self.message_user(request, '{} prints have been set to Sale'.format(count))
    set_print_to_sale.short_description = 'Mark selected prints for sale.'

# SETS THE SELECTED PRINTS PROMOTION STATUS TO FEATURE

    def set_print_to_feature(self, request, queryset):
        count = queryset.update(promotion='FEA')
        self.message_user(request, '{} prints have been set to Feature'.format(count))
    set_print_to_feature.short_description = 'Mark selected prints for feature.'

# SETS THE SELECTED PRINTS PROMOTION STATUS TO SPECIAL

    def set_print_to_special(self, request, queryset):
        count = queryset.update(promotion='SPE')
        self.message_user(request, '{} prints have been set to Special'.format(count))
    set_print_to_sale.special_description = 'Mark selected prints for special.'

# SETS THE SELECTED PRINTS PROMOTION STATUS TO NONE

    def set_print_to_none(self, request, queryset):
        count = queryset.update(promotion='NAN')
        self.message_user(request, '{} prints have been set to None'.format(count))
    set_print_to_sale.short_none = 'Mark selected prints as none.'

# SETS THE SELECTED PRINTS TO DISABLED

    def set_print_to_disabled(self, request, queryset):
        count = queryset.update(enable=False)
        self.message_user(request, '{} prints have been disabled'.format(count))
    set_print_to_sale.short_disabled = 'Mark selected prints as disabled.'

# SETS THE SELECTED PRINTS TO ENABLED

    def set_print_to_enabled(self, request, queryset):
        count = queryset.update(enable=True)
        self.message_user(request, '{} prints have been enabled'.format(count))
    set_print_to_sale.short_enabled = 'Mark selected prints as enabled.'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Print, PrintAdmin)
# Register your models here.

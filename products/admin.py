from django.contrib import admin
from .models import Product
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ['description', 'display_photo', 'price', 'discount']
    search_fields = ['description']

    def display_photo(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
    display_photo.short_description = 'Photo'

admin.site.register(Product, ProductAdmin)
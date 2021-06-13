from django.contrib import admin
from shop.models.Product import Product
from shop.models.Category import Category
from shop.models.Contact import Contact
from shop.models.ImageProduct import ImageProduct
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'detail',
        'price',
        'created_datetime',
        'updated_datetime',
        'is_recomment',
        'is_activate',
    )
    list_editable = (
        'is_activate',
        'is_recomment',
    )
    list_filter = (
        'category',
       'is_activate',
       'is_recomment',
    )
    search_fields = (
        'name',
    )
admin.site.register(Product,ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product',
        'message',
        'datetime',
        'is_enabled',
    )
    list_editable = (
        'is_enabled',
    )
    list_filter = (
        'name',
        'is_enabled'
    )
admin.site.register(Contact,ContactAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'detail',
        'image',
        'is_activate',
    )
    list_editable = (
        'is_activate',
    )
    list_filter = (
        'name',
        'is_activate'
    )
admin.site.register(Category,CategoryAdmin)

class ImageProductAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'images',
    )
    list_filter = (
        'product',
    )
admin.site.register(ImageProduct,ImageProductAdmin)

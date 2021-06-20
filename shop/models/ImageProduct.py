from django.db import models
from shop.models.Product import Product
from versatileimagefield.fields import VersatileImageField

class ImageProduct(models.Model):
    images = VersatileImageField(max_length=255,upload_to='images/products',default='',blank=True, null=True)
    # image = ImageCropField(blank=True, null=True, upload_to='images/products')
    # ImageField(upload_to='images')
    product = models.ForeignKey(Product, related_name='image',
                            on_delete=models.CASCADE, default=None, null=True)
    def __str__(self):
            return self.product.name

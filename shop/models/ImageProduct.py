from django.db import models
from shop.models.Product import Product
class ImageProduct(models.Model):
    images = models.ImageField(upload_to='images/products',max_length=900, default=None)
    product = models.ForeignKey(Product, related_name='image',
                            on_delete=models.CASCADE, default=None, null=True)
    def __str__(self):
            return self.product.name

from django.db import models
from shop.models.Category import Category
class Product(models.Model):
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=225)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name= 'products',default=None,null=True)
    price = models.IntegerField()
    is_recomment = models.BooleanField(default=True)
    is_activate = models.BooleanField(default=True)

    created_datetime = models.DateTimeField(auto_now=True)
    updated_datetime = models.DateTimeField(default=None,null=True)

    def save(self, *args, **kwargs):
            self.updated_datetime = datetime.datetime.now()
            super().save(*args, **kwargs)

    def __str__(self):
            return self.name


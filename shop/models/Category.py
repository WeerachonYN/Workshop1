from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=50)
    image =  models.ImageField(upload_to='image/categorys', max_length=900,default=None)
    detail = models.CharField(max_length=225)
    is_activate = models.BooleanField(default=True)

    def __str__(self):
            return self.name

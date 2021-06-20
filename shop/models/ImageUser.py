from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField

class ImageUser(models.Model):
    images = VersatileImageField(max_length=255,upload_to='images/user',default='',blank=True, null=True)

    user = models.OneToOneField(User, related_name='images',
                            on_delete=models.CASCADE, default=None, null=True)
    def __str__(self):
            return self.user.username

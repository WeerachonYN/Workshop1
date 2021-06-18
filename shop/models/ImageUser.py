from django.db import models
from django.contrib.auth.models import User
class ImageUser(models.Model):
    images = models.ImageField(upload_to='images/user',max_length=900, default=None)
    user = models.ForeignKey(User, related_name='images',
                            on_delete=models.CASCADE, default=None, null=True)
    def __str__(self):
            return self.user.username

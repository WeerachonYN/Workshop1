from django.db import models
from shop.models.Product import Product
from django.contrib.auth.models import User
class Contact(models.Model):
    first_name = models.CharField(max_length=50,help_text='กรุณากรอกชื่อ',error_messages={'required': 'กรุณากรอกชื่อ'})
    last_name = models.CharField(max_length=50,help_text='กรุณากรอกนามสกุล',error_messages={'required': 'กรุณากรอกนามสกุล'})
    email = models.EmailField(max_length=55,help_text='กรุณากรอกอีเมลล์',error_messages={'required': 'กรุณากรอกอีเมลล์'})
    messages = models.CharField(max_length=255,help_text='กรุณากรอกความคิดเห็น ไม่เกิน255ตัวอักษร',error_messages={'required': 'กรุณากรอกข้อความ'})
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE,default=None,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None,null=True)
    datetime = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=True)


    class Meta:
                ordering = ["-datetime"]

    def __str__(self):

            return self.messages

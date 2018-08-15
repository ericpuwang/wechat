from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user',
                                on_delete=models.CASCADE)
    wx_openid = models.CharField(max_length=64, unique=True)
    wx_pic = models.CharField(max_length=64, default='')
    phone = models.IntegerField()
    email = models.CharField(max_lenght=32)


class Remind(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                             related_name='remind')
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=2048)
    address = models.CharField(max_length=1024)
    remind_time = models.DateTimeField()
    status = models.CharField(max_length=32)

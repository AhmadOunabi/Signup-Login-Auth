from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Registration(models.Model):
    user=models.OneToOneField(User,related_name='registration',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.user.username
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser1(AbstractUser):

    gender = models.CharField(max_length=1, choices=(('m','M'),('f','F'),('o','O')), null=True, blank=True)
    age = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.gender

    # def __str__(self):
    #     return str(self.age) if self.age else ''
    #






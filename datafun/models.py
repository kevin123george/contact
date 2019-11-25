from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    userpic = models.ImageField(upload_to='users/', null=True, blank=True)
    Contact = models.IntegerField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

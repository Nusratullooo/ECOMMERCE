from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


# - - - - - - - - - - - - - - - CREATOR / ADMIN - - - - - - - - - - - - - - - #

class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(upload_to='images/Admin')

    def __str__(self):
        return self.user.username

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    def user_name(self):
        return self.user.first_name + '' + self.user.last_name + '[' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


# - - - - - - - - - - - - - - - CLIENT / USER - - - - - - - - - - - - - - - #

class Client(models.Model):
    STATUS = (
        ('True', 'ARE HAVE'),
        ('False', 'NOT HAVE'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=155)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/Clients')
    description = models.TextField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')

    def __str__(self):
        return self.user.username

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    def user_name(self):
        return self.user.first_name + '' + self.user.last_name + '[' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'

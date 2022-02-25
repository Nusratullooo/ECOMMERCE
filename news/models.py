from django.core.validators import FileExtensionValidator
from django.db import models


class News(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    user_name = models.CharField(max_length=55, blank=True)
    title = models.CharField(max_length=155, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/News',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])
    status = models.CharField(max_length=15, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name


class Comment_news(models.Model):
    STATUS = (
        ('TRUE', 'ARE HAVE'),
        ('FALSE', 'NOT HAVE'),
    )
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    comment = models.TextField(max_length=255, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

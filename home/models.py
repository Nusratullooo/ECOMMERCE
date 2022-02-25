from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# ---------- Information ---------- #

class Information(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(blank=True, max_length=20)
    email = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to='images/Info',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])
    telegram = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def info(self):
        information = Information.objects.all()
        return information

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


@receiver(pre_save, sender=Information)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Information.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


# ---------- ContactMessage ---------- #

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Read', "O'qilgan"),
        ('Closed', 'Yopilgan'),
    )
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField(max_length=255, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    ip = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ---------- FAQ ---------- #

class FAQ(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Yopilgan'),
    )
    question = models.TextField(max_length=255, blank=True)
    answer = models.TextField(max_length=255, blank=True)
    order_number = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


# ---------- / ABOUT US / ---------- #

class Aboutus(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/Aboutus',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


@receiver(pre_save, sender=Aboutus)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Aboutus.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


# ---------- / ABOUT US / ---------- #

class Slider(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/Slider',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


@receiver(pre_save, sender=Slider)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Slider.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


# ---------- NewsLetter ---------- #

class NewsLetter(models.Model):
    email = models.CharField(max_length=255)
    ip = models.CharField(blank=True, max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

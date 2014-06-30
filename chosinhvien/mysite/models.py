from django.db import models

# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=30)
    password = models.TextField()
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    sex = models.BooleanField(default=0)
    birthday = models.DateField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    facebook = models.CharField(max_length=100)
    last_login = models.DateTimeField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey('Member')
    category = models.ForeignKey('Category')
    price = models.IntegerField()
    image = models.FileField(upload_to='images/upload')
    quantity = models.IntegerField()
    time_post = models.DateField()
    status = models.BooleanField(default=0)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

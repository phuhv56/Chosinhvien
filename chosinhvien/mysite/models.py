from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    # user = models.ForeignKey('Member')
    category = models.ForeignKey('Category')
    value = models.IntegerField()
    image = models.ImageField(upload_to='images/upload/')
    quantity = models.IntegerField()
    time_post = models.DateField(auto_created=True)
    status = models.BooleanField(default=0)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
# Create your models here.


class Product(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    # user = models.ForeignKey('Member')
    category = models.ForeignKey('Category')
    value = models.IntegerField()
    image = models.ImageField(upload_to='images/upload/%y/%m', blank=True)
    quantity = models.IntegerField()
    time_post = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=0)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        s = self.name
        u = unicode(s)
        self.slug = slugify('%s %s %s' % (s, self.id, self.time_post, ))
        super(Product, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

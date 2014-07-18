# __author__ = 'Der Kaiser'

from django import forms
from django.forms import ModelForm
from mysite.models import Category, Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('slug', 'time_post', 'status', 'id', )


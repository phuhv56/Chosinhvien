from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context
from mysite.models import Product, Category
from django.template.loader import get_template

# Create your views here.


def show_all(request):
    products = Product.objects.all().order_by('time_post')
    context = {'products': products}
    return render_to_response('show_all.html', context)

# def product_detail(request, )
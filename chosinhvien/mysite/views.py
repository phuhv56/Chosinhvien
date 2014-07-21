from django.core.context_processors import csrf
from django.core.files.uploadhandler import FileUploadHandler
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response
from django.template import RequestContext, Context
from mysite.models import Product, Category
from django.template.loader import get_template
from forms import ProductForm
from django.http import HttpResponseRedirect

# Create your views here.


def show_all(request):
    user = ''
    if 'user' in request.COOKIES:
        user = request.COOKIES['user']
    products = Product.objects.all().order_by('-time_post')

    paginator = Paginator(products, 3) # show 3 products per page
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'products': products, 'user': user}
    return render_to_response('show_all.html', context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {'product': product}
    return render_to_response('product_detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            FileUploadHandler(request.FILES['image'])
            form.save()
            return HttpResponseRedirect('/show/all/')
    else:
        form = ProductForm()

    context = {'form': form}
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_product.html', args)
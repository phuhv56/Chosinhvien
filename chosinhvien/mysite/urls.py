# __author__ = 'Der Kaiser'


from django.conf.urls import include, url, patterns

urlpatterns = patterns(
    '',
    url(r'^all/$', 'mysite.views.show_all'),
    url(r'^product/(?P<product_slug>.*)/$', 'mysite.views.product_detail'),
    url(r'^create/$', 'mysite.views.create'),
)
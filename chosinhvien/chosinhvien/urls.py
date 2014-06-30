from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chosinhvien.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^show/', include('mysite.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

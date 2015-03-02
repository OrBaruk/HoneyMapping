from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),    
    url(r'^report/(\d{4})/(\d{2})/(\d{2})$', views.report, name='index'),    
)
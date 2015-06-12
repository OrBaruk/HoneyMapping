from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),    
	url(r'^teste/(\d{4})/(\d{1,2})/(\d{1,2})$', views.teste, name='index'),    
	url(r'^report/(\d{4})/(\d{1,2})$', views.report_month, name='index'),    
	url(r'^report/(\d{4})/(\d{1,2})/(\d{1,2})$', views.report_day, name='index'),    
)

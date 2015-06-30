from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views import generic

from main.models import IpLocation, Attack, Source
import datetime
import json

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def report_month(request, year, month):
	sources = Source.objects.all().filter(attack__dateTime__year=year, attack__dateTime__month=month)
	
	count   = dict()
	markers = dict()
	regions = dict()

	i = 0
	for s in sources:
		l 		= s.location
		cc		= l.countryCode
		size 	= 1 # s.quantity	

		if l.pk in markers:
			count[l.pk] = count[l.pk] + size
		else:
			print(i)
			i = i + 1
		
			m = dict()
			m['name']  	= s.protocol
			m['port']  	= s.port
			m['ip']    	= l.pk
			m['count'] 	= size
			m['latLng']	= [str(l.latitude), str(l.longitude)]
			m['city']  	= l.cityName
			m['countryCode'] = cc
			m['collector'] = s.collector
			markers[l.pk] = m
			count[l.pk] = size

		if cc in regions:
			regions[cc] += size
		else:
			regions[cc] = size

	mapdata = dict()
	mapdata['markers'] = list(markers.values())
	mapdata['count'] = list(count.values())
	mapdata['regions'] = regions

	return render(request, 'main/teste.html')
#	return HttpResponse(json.dumps(mapdata))

def report_day(request, year, month, day):
	sources = Source.objects.all().filter(attack__dateTime__year=year, attack__dateTime__month=month, attack__dateTime__day=day)
	
	count   = dict()
	markers = dict()
	regions = dict()

	for s in sources.iterator():
		l 		= s.location
		cc		= l.countryCode
		size 	= s.quantity	

		if l.pk in markers:
			count[l.pk] = count[l.pk] + size
		else:
			m = dict()
			m['name']  	= s.protocol
			m['port']  	= s.port
			m['ip']    	= l.pk
			m['count'] 	= size
			m['latLng']	= [str(l.latitude), str(l.longitude)]
			m['city']  	= l.cityName
			m['countryCode'] = cc
			m['collector'] = s.collector
			markers[l.pk] = m
			count[l.pk] = size

		if cc in regions:
			regions[cc] += size
		else:
			regions[cc] = size

	mapdata = dict()
	mapdata['markers'] = list(markers.values())
	mapdata['count'] = list(count.values())
	mapdata['regions'] = regions

	return HttpResponse(json.dumps(mapdata))

def teste(request, year, month, day):
	sources = Source.objects.all().filter(attack__dateTime__year=year, attack__dateTime__month=month, attack__dateTime__day=day)
	

	i = 0
	for s in Attack.objects.all():
		i = i + 1

	print(i)

	return render(request, 'main/teste.html')

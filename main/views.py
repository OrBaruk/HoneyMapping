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

	for s in sources:
		l 		= s.location
		cc		= l.countryCode
		size 	= s.quantity	

		m = dict()
		m['name']  	= s.protocol
		m['port']  	= s.port
		m['ip']    	= l.pk
		m['count'] 	= size
		m['latLng']	= [str(l.latitude), str(l.longitude)]
		m['city']  	= l.cityName
		m['countryCode'] = cc
		m['collector'] = s.collector

		if l.pk in markers:
			count[l.pk] = count[l.pk] + size
		else:
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

def report_day(request, year, month, day):
	sources = Source.objects.all().filter(attack__dateTime__year=year, attack__dateTime__month=month, attack__dateTime__day=day)
	
	count   = dict()
	markers = dict()
	regions = dict()

	for s in sources:
		l 		= s.location
		cc		= l.countryCode
		size 	= s.quantity	

		m = dict()
		m['name']  	= s.protocol
		m['port']  	= s.port
		m['ip']    	= l.pk
		m['count'] 	= size
		m['latLng']	= [str(l.latitude), str(l.longitude)]
		m['city']  	= l.cityName
		m['countryCode'] = cc
		m['collector'] = s.collector

		if l.pk in markers:
			count[l.pk] = count[l.pk] + size
		else:
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

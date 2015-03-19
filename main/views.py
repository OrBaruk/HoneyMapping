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

def report(request, year, month, day):
	sources = Source.objects.all().filter(attack__dateTime__year=year, attack__dateTime__month=month, attack__dateTime__day=day)
	
	count   = []
	markers = []
	regions = dict()

	for s in sources:
		attacks = Attack.objects.all().filter(source=s.pk)
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
		markers.append(m)

		if cc in regions:
			regions[cc] += size
		else:
			regions[cc] = size

		count.append(size)


	mapdata = dict()
	mapdata['markers'] = markers
	mapdata['count'] = count
	mapdata['regions'] = regions

	return HttpResponse(json.dumps(mapdata))
	# return HttpResponse(serializers.serialize('json', sources))
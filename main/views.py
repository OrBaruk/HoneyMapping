from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views import generic

from main.models import IpLocation, Attack, Source
import datetime
import json

from django.db import connection
import time

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
	#REQUIRES CHARACTER ESCAPING 
	cursor = connection.cursor()
	cursor.execute("select distinct ip_locations.ip, sources.port, sources.protocol, ip_locations.cityName, ip_locations.countryCode, ip_locations.latitude, ip_locations.longitude, sources.collector from attacks inner join sources on attacks.source_id == sources.id inner join ip_locations on ip_locations.ip == sources.location_id  where dateTime between '2014-08-14' and '2014-09-14 23:59:59'")

	count   = dict()
	markers = dict()
	regions = dict()

	start = time.time()	
	row = cursor.fetchone()
	while row:
		ip = row[0]
		port = row[1]
		protocol = row[2]
		city = row[3]
		countryCode = row[4]
		latitude = row[5]
		longitude = row[6]
		collector = row[7]

		cursor2 = connection.cursor()
		cursor2.execute("select count(ip_locations.ip)from attacks inner join sources on attacks.source_id == sources.id inner join ip_locations on ip_locations.ip == sources.location_id  where  ip='"+ip+"' and port='"+str(port)+"' and dateTime between '2014-08-14' and '2014-09-14 23:59:59'")
		quantity = cursor2.fetchone()[0] #querydecount

		m = dict()
		m['name']  	= protocol
		m['port']  	= port
		m['ip']    	= ip
		m['count'] 	= quantity
		m['latLng']	= [str(latitude), str(longitude)]
		m['city']  	= city
		m['countryCode'] = countryCode
		m['collector'] = collector

		markers[ip] = m
		count[ip] = quantity
		if countryCode in regions:
			regions[countryCode] += quantity
		else:
			regions[countryCode] = quantity

		row = cursor.fetchone()

	end = time.time()
	print(end - start)

	mapdata = dict()
	mapdata['markers'] = list(markers.values())
	mapdata['count'] = list(count.values())
	mapdata['regions'] = regions

	# return render(request, 'main/teste.html')
	return HttpResponse(json.dumps(mapdata))
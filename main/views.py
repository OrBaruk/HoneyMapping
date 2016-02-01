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

def report(request, startYear, startMonth, startDay, startHour, startMinute, endYear, endMonth, endDay, endHour, endMinute):	
	#Undefined behaviour for invalid dates
	if len(startDay) == 1:
		startDay = '0'+startDay 
	if len(endDay) == 1:
		endDay = '0'+endDay 

	start = time.time()	

	# if len(endDay) == 1:
	# 	startDay = '0'+startDay
	# if len(endDay) == 1:
	# 	endDay = '0'+endDay

	startDate = startYear+'-'+startMonth+'-'+startDay+' '+startHour+':'+startMinute+':00'
	endDate   = endYear+'-'+endMonth+'-'+endDay+' '+endMinute+':'+endHour+':59'

	print(startDate)
	print(endDate)

	cursor = connection.cursor()
	queryString = ( "SELECT DISTINCT "
						"ip_locations.ip, "
						"sources.port, "
						"sources.protocol, "
						"ip_locations.cityName, "
						"ip_locations.countryCode, "
						"ip_locations.latitude, "
						"ip_locations.longitude, "
						"sources.collector "
					"FROM attacks "
					"INNER JOIN sources ON attacks.source_id == sources.id "
					"INNER JOIN ip_locations ON ip_locations.ip == sources.location_id "
					"WHERE dateTime BETWEEN ? AND ?")
	cursor.execute(queryString, (startDate, endDate)) #sql wrapers escapes characters if needed

	count   = dict()
	markers = dict()
	regions = dict()

	row = cursor.fetchone()
	while row:
		ip 			= row[0]
		port 		= row[1]
		protocol 	= row[2]
		city 		= row[3]
		countryCode = row[4]
		latitude 	= row[5]
		longitude 	= row[6]
		collector 	= row[7]

		cursor2 = connection.cursor()
		queryString = ( "SELECT COUNT(ip_locations.ip) "
						"FROM attacks "
						"INNER JOIN sources ON attacks.source_id == sources.id "
						"INNER JOIN ip_locations ON ip_locations.ip == sources.location_id  "
						"WHERE ip=? AND port=? AND dateTime BETWEEN ? AND ?")
		cursor2.execute(queryString, (ip, port, startDate, endDate))
		quantity = cursor2.fetchone()[0]

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


	mapdata = dict()
	mapdata['markers'] = list(markers.values())
	mapdata['count'] = list(count.values())
	mapdata['regions'] = regions

	end = time.time()
	print(end - start)

	return HttpResponse(json.dumps(mapdata))
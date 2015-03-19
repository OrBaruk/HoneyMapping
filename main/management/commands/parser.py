from django.core.management.base import BaseCommand, CommandError
from main.models import IpLocation, Attack, Source

import GeoIP
import json
import os


class Command(BaseCommand):
	args = '<agr1> <arg2> ...'
	help = 'Some usefull help message'

	def handle(self, *args, **options):
		self.stdout.write('Hello handle')

		#call function to parse the logs
		parse_logs('/Users/or/LAS/HoneyMapping/data/unicamp.txt', 'testing_logparser', '/usr/local/share/GeoIP/GeoIPCity.dat')
		#delete the log files

		return


def parse_logs(filepath, collectorName, geoIPLibpath):
	# geoIPLibpath = "/usr/local/share/GeoIP/GeoIPCity.dat"

	gi = GeoIP.open(geoIPLibpath, GeoIP.GEOIP_STANDARD)
	f = open(filepath, 'r')
	
	for line in f.readlines():

		print(line)

		rows = line.split(' ')
		if len(rows) != 9:# Checks if the line has correct parameters
		    continue

		month	  = rows[5]
		day  	  = rows[6]
		time 	  = rows[7]

		aux	 = rows[8].split('-')
		if len(aux) != 4: # Checks if the line has correct parameters
			continue

		protc     = aux[0]
		port	  = aux[1]
		ipAddress = aux[2]
		hashKey   = aux[3]

		#Obtains geographic information from ip address
		gir = gi.record_by_addr(ipAddress)
		if gir:
			if gir['city']:
				city =  str(gir['city']) # Converts the string from Latin-1 according to GeoIP documentation
			else:
				city = 'Unknonw'
	
			lat = gir['latitude']
			lon = gir['longitude']
			cc = str(gir['country_code'])
		else:
			print("Ip not found in ipDatabase")
			city = 'Unknonw'
			lat = '0'
			lon = '0'
			cc  = '??'

		#Dictionary to translate the name to the month to expected number
		monthNumber = {
			'Jan' : '01',
			'Feb' : '02',
			'Mar' : '03',
			'Apr' : '04',
			'May' : '05',
			'Jun' : '06',
			'Jul' : '07',
			'Aug' : '08',
			'Sep' : '09',
			'Oct' : '10',
			'Nov' : '11',
			'Dec' : '12',
		}

		#Saves information into database
		l = IpLocation(
				ip       	= ipAddress,
				latitude 	= lat, 
				longitude	= lon,
				cityName 	= city,
				countryCode = cc
			)
		l.save()
		s , created = Source.objects.get_or_create(
				location  = l,
				port	  = port,
				collector = collectorName,
				protocol  = protc,
			)
		s.quantity = s.quantity + 1
		s.save()
		a = Attack(
				key		  = hashKey,
				dateTime  = '2015-'+monthNumber[month]+'-'+day+' '+time,
				source    = s,
			)
		a.save()
from django.core.management.base import BaseCommand, CommandError
from main.models import IpLocation, Attack, Source

import GeoIP
import json
import os


class Command(BaseCommand):
	args = '<agr1> <arg2> ...'
	help = 'Some usefull help message'

	def handle(self, *args, **options):
		self.stdout.write(args[0])

		#call function to parse the logs
		parse_logs('/Users/or/LAS/HoneyMapping/data/logs_jul2015/'+args[0]+'.txt', args[0], '/usr/local/share/GeoIP/GeoIPCity.dat')

		return


def parse_logs(filepath, collectorName, geoIPLibpath):
	# geoIPLibpath = "/usr/local/share/GeoIP/GeoIPCity.dat"

	gi = GeoIP.open(geoIPLibpath, GeoIP.GEOIP_STANDARD)
	f = open(filepath, 'r')
	
	for line in f.readlines():
		#print(line)


		rows = line.split()		
		if len(rows) != 9:# Checks if the line has correct parameters
			continue
		#print(rows[8])

		m = dict()
		m['Jan'] = '01'
		m['Feb'] = '02'
		m['Mar'] = '03'
		m['Apr'] = '04'
		m['May'] = '05'
		m['Jun'] = '06'
		m['Jul'] = '07'

		aux = rows[5].split('-')
		year	  = '2015' #aux[0]		
		month	  = m[rows[5]] #aux[1]
		day  	  = rows[6] #aux[2]

		#print(rows[5]+' '+rows[6])

		time 	  = rows[7]

		aux	 = rows[8].split('-')
		if len(aux) != 4: # Checks if the line has correct parameters
			continue
		print(year+'-'+month+'-'+day+"\t"+rows[8])

		protc     = aux[0]
		port	  = aux[1]
		ipAddress = aux[2]
		hashKey   = aux[3]

		#Obtains geographic information from ip address
		gir = gi.record_by_addr(ipAddress)
		if gir:
			#if gir['city']:
			city =  str(gir['city']) # Converts the string from Latin-1 according to GeoIP documentation
			#else:
			#	city = 'Unknonw'
	
			lat = gir['latitude']
			lon = gir['longitude']
			cc = str(gir['country_code'])
		else:
			print("Ip not found in ipDatabase")
			city = 'Unknonw'
			lat = '0'
			lon = '0'
			cc  = '??'


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
				dateTime  = year+'-'+month+'-'+day+' '+time, #rows[5]+' '+rows[6],

				source    = s,
			)
		a.save()
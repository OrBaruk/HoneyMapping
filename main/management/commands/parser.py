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
		# geoIPLibpath = "/usr/local/share/GeoIP/GeoIPCity.dat"
		parse_logs(args[0], args[1], args[2])

		return


def parse_logs(filepath, collectorName, geoIPLibpath):
	gi = GeoIP.open(geoIPLibpath, GeoIP.GEOIP_STANDARD)
	f = open(filepath, 'r')

	for line in f.readlines():

		rows = line.split()
		if len(rows) != 8:# Checks if the line has correct parameters
			print('oito?')
			continue


		aux	 = rows[7].split('-')
		if len(aux) != 4: # Checks if the line has correct parameters
			continue

		print(line),
		
		protc     = aux[0]
		port	  = aux[1]
		ipAddress = aux[2]
		hashKey   = aux[3]

		#Obtains geographic information from ip address
		gir = gi.record_by_addr(ipAddress)
		if gir:
			# Converts the string from Latin-1 according to GeoIP documentation
			city =  str(gir['city'])

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
				dateTime  = rows[5]+' '+rows[6],
				source    = s,
			)
		a.save()

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

############################
import GeoIP
import json
############################


class LogEntry:
	name = 'Unknonw Name'
	port = 0
	ip = []
	key = []
	date  = [] # Precisa ver qual lib de python utilizar
	city = 'Unknonw City'
	latLng = [0,0]
	countryCode = ''

	def __init__(self, name_, port_, ip_, key_, date_, city_, latLng_, countryCode_):
		self.name = name_
		self.port = port_ 
		self.ip = ip_ 
		self.key = key_ 
		self.date = date_ 
		self.city = city_
		self.latLng = latLng_
		self.countryCode = countryCode_


	def add_entry(self, ip_, key_, date_):
		self.ip.append(ip_)
		self.key.append(key_)
		self.date.append(date_)

	def __str__(self):
		return str(self.key)

	def __repr__(self):
		return str(self.key)


def parse_logs(filepath, geoIPLibpath):
	geoIPLibpath = "/usr/local/share/GeoIP/GeoIPCity.dat"
	gi = GeoIP.open(geoIPLibpath, GeoIP.GEOIP_STANDARD)
	f = open(filepath, 'r')
	
	d = dict()

	for line in f.readlines():
		rows = line.split('-')

		if len(rows) != 4: # Caso o log file seja invalido
			continue 

		gir = gi.record_by_addr(rows[2])
		if gir:
			key = rows[0]+';'+rows[1]+';'+str(gir['latitude'])+';'+str(gir['longitude'])
			if gir['city']:
				city =  unicode(gir['city'], 'latin1') # Converte a string de Latin-1 segundo a documentacao do GeoIP
			else:
				city = 'Unknonw'

			latLng = [gir['latitude'], gir['longitude']]
			countryCode = unicode(gir['country_code'], 'latin1')

		else:
			print "Error on gir"


		if key in d:
			d[key].add_entry([rows[2]], [rows[3]],['datahora'])
		else:
			d[key] = LogEntry(rows[0], rows[1], [rows[2]], [rows[3]], ['datahora'], city, latLng, countryCode)
		
	f.close()

	return d

# Create your views here.
def index(request):
	# Arrays data are passed to map.js
	markers = []
	count = []
	regions = []

	d = parse_logs('data/logs.txt', '/usr/local/share/GeoIP/GeoIPCity.dat')

	i = 0
	countSet = []
	markersSet = []
	regionsSet = dict()
	for key in d.keys():
		if i == 10:
			i = 0;
			markers.append(markersSet)
			count.append(countSet)
			regions.append(regionsSet)
			countSet = []
			markersSet = []
			regionsSet = dict()

		le = dict()
		le['name'] = d[key].name
		le['port'] = d[key].port
		le['ip'] = d[key].ip
		le['count'] = len(d[key].key)
		le['latLng'] = d[key].latLng
		le['city'] = d[key].city

		cc = d[key].countryCode
		le['countryCode'] = cc

		if cc in regionsSet:
			regionsSet[cc] += le['count']
		else:
			regionsSet[cc] = le['count']

		markersSet.append(le)


		for le in markersSet:
			countSet.append(le['count'])

		i += 1
	markers.append(markersSet)
	count.append(countSet)
	regions.append(regionsSet)



	pd = dict()
	# Count by the attacks type
	for markersSet in markers:
		for le in markersSet:
			key = le['name']+':'+le['port']
			if key in pd:
				pd[key] += le['count']
			else:
				pd[key] = le['count']

	# Translate pd to the json format expected by d3.js
	piedata = []
	for key in pd:
		d = dict()
		d['label'] = key
		d['value'] = pd[key]

		piedata.append(d)

	return render(request, 'main/index.html', {
			'markers' : json.dumps(markers),
			'count'   : json.dumps(count),
			'regions' : json.dumps(regions),
			'piedata' : json.dumps(piedata),
		})
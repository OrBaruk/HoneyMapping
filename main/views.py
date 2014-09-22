from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Poll

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

	def __init__(self, name_, port_, ip_, key_, date_, city_, latLng_):
		self.name = name_
		self.port = port_ 
		self.ip = ip_ 
		self.key = key_ 
		self.date = date_ 
		self.city = city_
		self.latLng = latLng_


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

		key = rows[0]+';'+rows[1]+';'+str(gir['latitude'])+';'+str(gir['longitude'])
		city =  gir['city']
		latLng = [gir['latitude'], gir['longitude']]
		
		if key in d:
			d[key].add_entry([rows[2]], [rows[3]],['datahora'])
		else:
			d[key] = LogEntry(rows[0], rows[1], [rows[2]], [rows[3]], ['datahora'], city, latLng )
		
	f.close()

	return d

# Create your views here.
def index(request):
	return render(request, 'main/index.html')


def jvectormap(request):
	markers = []
	count = []
	d = parse_logs('data/logs.txt', '/usr/local/share/GeoIP/GeoIPCity.dat')

	for key in d.keys():
		le = dict()
		le['name'] = d[key].name
		le['port'] = d[key].port
		le['ip'] = d[key].ip
		le['count'] = len(d[key].key)
		le['latLng'] = d[key].latLng
		le['city'] = d[key].city

		markers.append(le)

	for le in markers:
		count.append(le['count'])

	pd = dict()

	# Count by the attacks type
	for le in markers:
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

	return render(request, 'main/jvectormap.html', {
			'markers' : json.dumps(markers),
			'count' : json.dumps(count),
			'piedata' : json.dumps(piedata),
		})
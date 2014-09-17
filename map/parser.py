import GeoIP
import json

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
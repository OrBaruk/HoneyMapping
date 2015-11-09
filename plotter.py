import sqlite3
import matplotlib.pyplot as plt
import datetime as datetime

def plot_attacks_all():
	cursor = sqlite3.connect('db.sqlite3').cursor()
	query = ("SELECT COUNT(*)"
			" FROM attacks"
			" WHERE  attacks.dateTime BETWEEN ? AND ?"
			" ORDER BY attacks.dateTime ASC")

	initialDay = datetime.datetime(2014,10,6)
	finalDay = datetime.datetime(2015,7,14)

	start  = initialDay
	end = initialDay + datetime.timedelta(hours=23, minutes=59)

	x = []
	y = []

	totalDays = 0
	average = 0

	while start < finalDay:
		cursor.execute(query, (start, end))

		x.append(start)
		aux = cursor.fetchone()[0]
		y.append(aux)
		average += aux 
		totalDays += 1

		start = start + datetime.timedelta(days=1)
		end = end + datetime.timedelta(days=1)

	average = average / totalDays
	print(totalDays)
	print(average)


	plt.plot(x, y, color='black')
	plt.fill_between(x, 0, y, color='black')
	plt.ylabel('Número de Conexões')
	plt.show()


def plot_attacks_distinct():
	cursor = sqlite3.connect('db.sqlite3').cursor()
	query = ("SELECT COUNT(DISTINCT attacks.source_id)"
			" FROM attacks"
			" WHERE  attacks.dateTime BETWEEN ? AND ?"
			" ORDER BY attacks.dateTime ASC")
	initialDay = datetime.datetime(2014,10,6)
	finalDay = datetime.datetime(2015,7,14)

	start  = initialDay
	end = initialDay + datetime.timedelta(hours=23, minutes=59)

	x = []
	y = []

	totalDays = 0
	average = 0
	while start < finalDay:
		totalDays += 1

		cursor.execute(query, (start, end))

		x.append(start)
		aux = cursor.fetchone()[0]
		y.append(aux)

		average += aux 

		start = start + datetime.timedelta(days=1)
		end = end + datetime.timedelta(days=1)

	average = average / totalDays
	print(totalDays)
	print(average)

	plt.plot(x, y, color='black')
	plt.fill_between(x, 0, y, color='black')
	plt.ylabel('Número de Conexões Únicas')
	plt.show()


def plot_histogram():
	cursor = sqlite3.connect('db.sqlite3').cursor()
	query = ("SELECT strftime('%H', dateTime)"
			" FROM attacks")

	y = [0 for i in range(0,24)]

	cursor.execute(query)	
	row = cursor.fetchone()
	while row:
		y[int(row[0])] = y[int(row[0])] + 1
		row = cursor.fetchone()

	x = range(len(y))
	width = 1/1.5

	plt.bar(x,y, width, color='black')
	plt.xlabel('Hora do Ataque')
	plt.ylabel('Número de Conexões')
	plt.xlim([0,24])
	plt.show()


def plot_histogram_distinct():
	cursor = sqlite3.connect('db.sqlite3').cursor()
	query = ("SELECT strftime('%H', dateTime), source_id"
			" FROM attacks"
			" GROUP BY source_id")

	y = [0 for i in range(0,24)]

	cursor.execute(query)	
	row = cursor.fetchone()
	while row:
		y[int(row[0])] = y[int(row[0])] + 1
		row = cursor.fetchone()

	x = range(len(y))
	width = 1/1.5

	plt.bar(x,y, width, color='black')
	plt.xlabel('Hora do Ataque')
	plt.ylabel('Número de Conexões Únicas')
	plt.xlim([0,24])
	plt.show()


def plot_histogram_protocol(port):
	# portas na base 21, 80, 135, 445, 1433, 5060
	cursor = sqlite3.connect('db.sqlite3').cursor()
	query = ("SELECT strftime('%H', attacks.dateTime), attacks.source_id"
			" FROM attacks"
			" INNER JOIN sources ON attacks.source_id == sources.id"
			" WHERE sources.port == ?"
			)

	y = [0 for i in range(0,24)]

	cursor.execute(query,(port,))	
	row = cursor.fetchone()
	while row:
		y[int(row[0])] = y[int(row[0])] + 1
		row = cursor.fetchone()

	x = range(len(y))
	width = 1/1.5

	plt.bar(x,y, width, color='black')
	plt.xlabel('Hora do Ataque')
	plt.ylabel('Número de Conexões')
	plt.xlim([0,24])
	plt.show()

def plot_histogram_protocol_not(port):
	# portas na base 21, 80, 135, 445, 1433, 5060
	cursor = sqlite3.connect('db.sqlite3').cursor()
	query = ("SELECT strftime('%H', attacks.dateTime), attacks.source_id"
			" FROM attacks"
			" INNER JOIN sources ON attacks.source_id == sources.id"
			" WHERE sources.port != ?"
			)

	y = [0 for i in range(0,24)]

	cursor.execute(query,(port,))	
	row = cursor.fetchone()
	while row:
		y[int(row[0])] = y[int(row[0])] + 1
		row = cursor.fetchone()

	x = range(len(y))
	width = 1/1.5

	plt.bar(x,y, width, color='black')
	plt.xlabel('Hora do Ataque')
	plt.ylabel('Número de Conexões')
	plt.xlim([0,24])
	plt.show()

def plot_histogram_distinct_protocol(port):
	# portas na base 21, 80, 135, 445, 1433, 5060
	cursor = sqlite3.connect('db.sqlite3').cursor()
	query = ("SELECT strftime('%H', attacks.dateTime), attacks.source_id"
			" FROM attacks"
			" INNER JOIN sources ON attacks.source_id == sources.id"
			" WHERE sources.port == ?"
			" GROUP BY attacks.source_id"
			)

	y = [0 for i in range(0,24)]

	cursor.execute(query,(port,))	
	row = cursor.fetchone()
	while row:
		y[int(row[0])] = y[int(row[0])] + 1
		row = cursor.fetchone()

	x = range(len(y))
	width = 1/1.5

	plt.bar(x,y, width, color='black')	
	plt.xlabel('Hora do Ataque')
	plt.ylabel('Número de Conexões Únicas')
	plt.xlim([0,24])
	plt.show()


def generate_report():
	cursor = sqlite3.connect('db.sqlite3').cursor()
	initialDay = datetime.datetime(2014,10,6)
	finalDay = datetime.datetime(2015,7,15)
	ports = [21, 80, 135, 445, 1433, 5060]

	delta = datetime.timedelta(days=300000000)
	# start = datetime.datetime(2014,10,1)
	# end = start + delta
	
	start = initialDay
	end = finalDay

	while start < finalDay:
		print("Start: ", start)
		print("End:   ", end)

		query = ("SELECT COUNT(*)"
				" FROM attacks"
				" WHERE attacks.dateTime BETWEEN ? AND ?")
		cursor.execute(query, (start, end))
		total = cursor.fetchone()[0]
		print("Total Attacks: ", total)

		for p in ports:
			query = ("SELECT COUNT(*)"
					" FROM attacks"
					" INNER JOIN sources ON attacks.source_id == sources.id"
					" WHERE sources.port=? AND attacks.dateTime BETWEEN ? AND ?")		
			cursor.execute(query, (p, start, end))
			aux = cursor.fetchone()[0]
			print("> %4d: %8d | %2.2f" % (p, aux, 100*aux/total),'%')


		query = ("SELECT COUNT(DISTINCT attacks.source_id)"
				" FROM attacks"
				" WHERE attacks.dateTime BETWEEN ? AND ?")
		cursor.execute(query, (start, end))
		total = cursor.fetchone()[0]
		print("Distintc Attack Sources: ", total)

		for p in ports:
			query = ("SELECT COUNT(DISTINCT source_id)"
					" FROM attacks"
					" INNER JOIN sources ON attacks.source_id == sources.id"
					" WHERE sources.port=? AND attacks.dateTime BETWEEN ? AND ?")
			cursor.execute(query, (p, start, end))
			aux = cursor.fetchone()[0]
			print("> %4d: %8d | %2.2f" % (p, aux, 100*aux/total),'%')

		query = ("SELECT COUNT(DISTINCT ip_locations.ip)"
				" FROM attacks"
				" INNER JOIN sources ON attacks.source_id == sources.id"
				" INNER JOIN ip_locations ON ip_locations.ip == sources.location_id"
				" WHERE attacks.dateTime BETWEEN ? AND ?")
		cursor.execute(query, (start, end))
		total = cursor.fetchone()[0]
		print("Unique IPlocations: ", total)

		start  = start + delta
		end = end + delta

def locations_report():
	cursor = sqlite3.connect('db.sqlite3').cursor()
	initialDay = datetime.datetime(2014,10,6)
	finalDay = datetime.datetime(2015,7,14)
	ports = [21, 80, 135, 445, 1433, 5060]

	query = ("SELECT ip_locations.ip, sources.collector"
			" FROM attacks"
			" INNER JOIN sources ON attacks.source_id == sources.id"
			" INNER JOIN ip_locations ON ip_locations.ip == sources.location_id"
			" WHERE attacks.dateTime BETWEEN ? AND ?")

	cursor.execute(query, (initialDay, finalDay))
	rows = cursor.fetchall()

	d = dict()
	for row in rows:
		if row[0] in d:
			d[row[0]].add(row[1])
		else:
			d[row[0]] = set()
			d[row[0]].add(row[1])
	
	#filter the dictionary to contais elements with more than size 1
	return {k: v for k, v in d.items() if len(v) > 1}


def locations_maxday():
	#ip de interesse: 211.20.56.85 (maior range)
	cursor = sqlite3.connect('db.sqlite3').cursor()
	initialDay = datetime.datetime(2014,10,6)
	finalDay = datetime.datetime(2015,7,14)
	ports = [21, 80, 135, 445, 1433, 5060]

	query = ("SELECT DISTINCT ip_locations.ip"
			" FROM ip_locations")
	cursor.execute(query)

	d = dict()

	row = cursor.fetchone()
	while row:
		ip = row[0]
		c = sqlite3.connect('db.sqlite3').cursor()
		query = ("SELECT attacks.dateTime"
				" FROM attacks"
				" INNER JOIN sources ON attacks.source_id == sources.id"
				" INNER JOIN ip_locations ON ip_locations.ip == sources.location_id"
				" WHERE ip_locations.ip == ?"
				" ORDER BY attacks.dateTime ASC")
		c.execute(query, (ip,))
		rows = c.fetchall()
		if rows:
			startDate = datetime.datetime.strptime(rows[0][0][:19],'%Y-%m-%d %H:%M:%S')
			endDate = datetime.datetime.strptime(rows[len(rows)-1][0],'%Y-%m-%d %H:%M:%S')
			d[ip] = endDate - startDate
	

		row = cursor.fetchone()

	x = []
	for v in d.values():
		x.append(v.days)
	xbins =range(365)

	# plt.hist(x, bins=xbins, log=True, color='black')
	# plt.xlabel('Número de Dias Operacionais')
	# plt.ylabel('IPs únicos')
	# plt.show()

	out = [0 for i in range(365)]
	days = range(365)
	for e in x:
		for day in days:
			if e >= day:
				out[day] += 1

	for day in days:
	 	out[day] = out[day]/len(x)

	aux = [1,7,30,60,90,120,150,180,210,240,270,300,330,360]
	for a in aux:
		print("%3d dias | %1.10f" % (a, out[a]))

	plt.plot(out, color='black')
	plt.xlabel('Numero de dias ativo')
	plt.ylabel('Fração dos IPs')
	plt.fill_between(days, 0, out, color='black')
	#plt.yscale('log')
	plt.xlim([0,365])
	plt.show()



def locations_total_connections():
	#ip de interesse: 211.20.56.85 (maior range)
	cursor = sqlite3.connect('db.sqlite3').cursor()
	initialDay = datetime.datetime(2014,10,6)
	finalDay = datetime.datetime(2015,7,14)
	ports = [21, 80, 135, 445, 1433, 5060]

	query = ("SELECT DISTINCT ip_locations.ip"
			" FROM ip_locations")
	cursor.execute(query)


	d = dict()
	return d


def plot_all():
	ports = [21, 80, 135, 445, 1433, 5060]

	locations_maxday()

	plot_attacks_all()
	plot_attacks_distinct()

	plot_histogram()
	plot_histogram_distinct()

	for port in ports:
		plot_histogram_protocol(port)
		plot_histogram_distinct_protocol(port)

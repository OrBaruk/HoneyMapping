from django.db import models

# Create your models here.
class IpLocation(models.Model):
	ip = models.GenericIPAddressField(protocol='IPv4',
									  unpack_ipv4=False,
									  unique=True,
									  primary_key=True)
	latitude = models.DecimalField(max_digits=6, decimal_places=2)
	longitude = models.DecimalField(max_digits=6, decimal_places=2)
	cityName =	models.CharField(max_length=255)
	countryCode = models.CharField(max_length=2)

	def __unicode__(self): # __unicode__ on Python 2
		return self.cityName+'['+self.latitude+','+self.longitude+']'

	class Meta:
		db_table = 'ip_locations'

class Target(models.Model):
	id = models.AutoField(primary_key=True)
	location = models.ForeignKey(IpLocation)
	port = models.IntegerField()
	collector = models.CharField(max_length=255)
	protocol = models.CharField(max_length=255)

	class Meta:
		db_table		= 'targets'
		unique_together = ('port','location','collector','protocol')

	def __unicode__(self): # __unicode__ on Python 2
		return self.collector+":"+self.port+'['+self.protocol+']'

class Attack(models.Model):
	key = models.CharField(max_length=255, 
	        			   unique=True,
	        			   primary_key=True) # Chech the maxlength of hash
	dateTime	= models.DateTimeField()
	target  	= models.ForeignKey(Target)

	def __unicode__(self): # __unicode__ on Python 2
		return self.attack+":"+self.key+'['+self.dateTime+']'

	class Meta:
		db_table = 'attacks'
from django.db import models

# Create your models here.
class ipLocation(models.Model):
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

class attack(models.Model):
	key = models.CharField(max_length=255, 
						   unique=True,
						   primary_key=True) # Chech the maxlength of hash
	date = models.DateField()
	location = models.ForeignKey(ipLocation)
	port = models.IntegerField()
	name = models.CharField(max_length=255)

	def __unicode__(self): # __unicode__ on Python 2
		return self.name+":"+self.port+'['+self.key+']'

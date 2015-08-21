from django.core.management.base import BaseCommand, CommandError
from main.models import IpLocation, Attack, Source

import GeoIP
import json
import os


class Command(BaseCommand):
	args = '<agr1> <arg2> ...'
	help = 'Some usefull help message'

	def handle(self, *args, **options):
		test()
		
		return


def test():
	sources = Source.objects.all().filter(attack__dateTime__year=2015, attack__dateTime__month=9, attack__dateTime__day=18)
	
	for s in sources:
		attacks = Attack.objects.all().filter(source=s.pk)
		size1 	= s.quantity	

		print('.', end='',flush=True)

	return
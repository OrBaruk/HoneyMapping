from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views import generic

from main.models import IpLocation, Attack, Source
import datetime
#import json

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def report(request, year, month, day):
	
	s = Source.objects.all().filter(attack__dateTime__year=year, attack__dateTime__month=month, attack__dateTime__day=day)
	j = serializers.serialize('json',s)

	for x in s:
		a = Attack.objects.all().filter(source=x.pk)

	return HttpResponse(j)
#!/bin/bash

mv /home/baruque/HoneyMapping/var/data/cti.txt /home/baruque/HoneyMapping/var/data/cti_tmp.txt 
python3 /home/baruque/HoneyMapping/manage.py parser /home/baruque/HoneyMapping/var/data/cti_tmp.txt cti /home/baruque/HoneyMapping/GeoIP-data/GeoIPCity.dat
rm /home/baruque/HoneyMapping/var/data/cti_tmp.txt 

mv /home/baruque/HoneyMapping/var/data/facom.txt /home/baruque/HoneyMapping/var/data/facom_tmp.txt 
python3 /home/baruque/HoneyMapping/manage.py parser /home/baruque/HoneyMapping/var/data/facom_tmp.txt facom /home/baruque/HoneyMapping/GeoIP-data/GeoIPCity.dat
rm /home/baruque/HoneyMapping/var/data/facom_tmp.txt 

mv /home/baruque/HoneyMapping/var/data/unicamp.txt /home/baruque/HoneyMapping/var/data/unicamp_tmp.txt 
python3 /home/baruque/HoneyMapping/manage.py parser /home/baruque/HoneyMapping/var/data/unicamp_tmp.txt unicamp /home/baruque/HoneyMapping/GeoIP-data/GeoIPCity.dat
rm /home/baruque/HoneyMapping/var/data/unicamp_tmp.txt 


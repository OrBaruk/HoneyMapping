#!/bin/bash

mv /home/baruque/HoneyMapping/var/data/cti.txt /home/baruque/HoneyMapping/var/data/cti_tmp.txt 
python3 /home/baruque/HoneyMapping/manage.py parser cti /home/baruque/HoneyMapping/var/data/cti_tmp.txt 
rm /home/baruque/HoneyMapping/var/data/cti_tmp.txt 

mv /home/baruque/HoneyMapping/var/data/facom.txt /home/baruque/HoneyMapping/var/data/facom_tmp.txt 
python3 /home/baruque/HoneyMapping/manage.py parser facom /home/baruque/HoneyMapping/var/data/facom_tmp.txt 
rm /home/baruque/HoneyMapping/var/data/facom_tmp.txt 

mv /home/baruque/HoneyMapping/var/data/unicamp.txt /home/baruque/HoneyMapping/var/data/unicamp_tmp.txt 
python3 /home/baruque/HoneyMapping/manage.py parser unicamp /home/baruque/HoneyMapping/var/data/unicamp_tmp.txt 
rm /home/baruque/HoneyMapping/var/data/unicamp_tmp.txt 


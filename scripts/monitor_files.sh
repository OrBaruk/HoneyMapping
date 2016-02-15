#!/bin/bash
nohup sh -c "fswatch -0 --event Created /home/pakkun/honey/cti/dionaea/bistreams | xargs -0 -n 1 -I {} /home/baruque/HoneyMapping/scripts/fswatch_launcher.sh {} cti" </dev/null >/dev/null 2>&1 &
echo $! >> /home/baruque/HoneyMapping/var/pid.txt

nohup sh -c "fswatch -0 --event Created /home/pakkun/honey/facom/dionaea/bistreams | xargs -0 -n 1 -I {} /home/baruque/HoneyMapping/scripts/fswatch_launcher.sh {} facom" </dev/null >/dev/null 2>&1 &
echo $! >> /home/baruque/HoneyMapping/var/pid.txt

nohup sh -c "fswatch -0 --event Created /home/pakkun/honey/unicamp/dionaea/bistreams | xargs -0 -n 1 -I {} /home/baruque/HoneyMapping/scripts/fswatch_launcher.sh {} unicamp" </dev/null >/dev/null 2>&1 &
echo $! >> /home/baruque/HoneyMapping/var/pid.txt

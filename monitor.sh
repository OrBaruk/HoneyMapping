#!/bin/bash
nohup fswatch -0 --event Created /home/pakkun/honey/cti/dionaea/bistreams/ | xargs -0 -n 1 -I {} /home/baruque/HoneyMapping/launch_monitor.sh {} cti &
nohup fswatch -0 --event Created /home/pakkun/honey/inpe/dionaea/bistreams/ | xargs -0 -n 1 -I {} /home/baruque/HoneyMapping/launch_monitor.sh {} inpe &
nohup fswatch -0 --event Created /home/pakkun/honey/facom/dionaea/bistreams/ | xargs -0 -n 1 -I {} /home/baruque/HoneyMapping/launch_monitor.sh {} facom &
nohup fswatch -0 --event Created /home/pakkun/honey/unicamp/dionaea/bistreams/ | xargs -0 -n 1 -I {} /home/baruque/HoneyMapping/launch_monitor.sh {} unicamp &

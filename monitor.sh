#!/bin/bash

nohup fswatch -r -0 --event Created /home/pakkun/honey/cti/var/dionaea/bistreams/ | xargs -0 -n 1 -I {} ls -la --time-style=long-iso {} >> /home/baruque/fswatch_test/"cti_first" &

fswatch -0 --event Created /home/pakkun/honey/cti/var/dionaea/bistreams/ | xargs -0 -n 1 -I {} /home/baruque/HoneyMapping/launch_monitor.sh {}

#TESTES
#nohup fswatch -r -0 --event Created /home/baruque/tmp/ | xargs -0 -n 1 -I {} ls -la --time-style=long-iso {} >> /home/baruque/fswatch_test/"cti_first" &

#fswatch -0 --event Created /home/baruque/tmp | xargs -0 -n 1 -I {} /home/baruque/HoneyMapping/launch_monitor.sh {}


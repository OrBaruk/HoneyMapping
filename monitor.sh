#!/bin/bash

#FSWatch folders usar supervise/daemontools
#fswatch -0 monitorado/ | xargs -0 -n 1 -I {} ls -la --time-style=long-iso {} >> logs.txt
#CRON  parser.py
#python mananage.py parser logs.txt
#fswatch -r --event Created -0 /home/pakkun/honey/cti/var/dionaea/bistreams/ | xargs -0 -n 1 -I {} ls -la --time-style=long-iso {} >> /home/baruque/fswatch_test/cti_logs.txt
#fswatch --event Created -0 /home/baruque/tmp/ | xargs -0 -n 1 -I {} fswatch --event Created {} >> /home/baruque/fswatch_test/teste1.txt 


fswatch -0 --event Created /home/baruque/fswatch_test | xargs -0 -n 1 -I {} /home/baruque/HoneyMapping/launch_monitor.sh {}



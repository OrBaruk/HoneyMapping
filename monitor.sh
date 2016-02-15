#!/bin/bash
nohup sh -c "fswatch -0 --event Created /home/baruque/tmp/tests/a1/ | xargs -0 -n 1 -I {} /home/baruque/tmp/launch_monitor.sh {} a1" </dev/null >/dev/null 2>&1 &
echo $! >> /home/baruque/tmp/pid.txt

nohup sh -c "fswatch -0 --event Created /home/baruque/tmp/tests/a2/ | xargs -0 -n 1 -I {} /home/baruque/tmp/launch_monitor.sh {} a2" </dev/null >/dev/null 2>&1 &
echo $! >> /home/baruque/tmp/pid.txt



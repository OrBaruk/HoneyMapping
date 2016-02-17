#!/bin/bash

path="${1:-/dev/stdin}"
nohup sh -c "fswatch -0 --event Created $path | xargs -0 -n 1 -I {} ls -la --time-style=long-iso {} >> /home/baruque/HoneyMapping/var/data/$2.txt" </dev/null >/dev/null 2>&1 &
echo $! >> /home/baruque/HoneyMapping/var/pid.txt


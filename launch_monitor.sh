#!/bin/bash

path="${1:-/dev/stdin}"
name=$(basename "$path" "")
nohup sh -c "fswatch -0 --event Created $path | xargs -0 -n 1 -I {} ls -la --time-style=long-iso {} >> /home/baruque/tmp/out/$name_$2" </dev/null >/dev/null>&1 &
echo $! >> /home/baruque/tmp/pid.txt


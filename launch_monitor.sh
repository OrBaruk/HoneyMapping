#!/bin/bash

path="${1:-/dev/stdin}"
name=$(basename "$path" "")
echo $path

nohup fswatch -0 --event Created $path | xargs -0 -n 1 -I {} ls -la --time-style=long-iso {} >> /home/baruque/fswatch_test/"cti_"$name &


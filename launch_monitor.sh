#!/bin/bash

path="${1:-/dev/stdin}"
name=$(basename "$path" "")

echo $path
echo $name

nohup fswatch -0 --event Created $path > $name &


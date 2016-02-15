#!/bin/bash
while read p; do
  pkill -TERM -P $p
done < $1
rm $1


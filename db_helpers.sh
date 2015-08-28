#!/bin/bash

#FSWatch folders usar supervise/daemontools
fswatch -0 monitorado/ | xargs -0 -n 1 -I {} ls -la --time-style=long-iso {} >> logs.txt

#CRON  parser.py
python mananage.py parser logs.txt

#!/usr/bin/env python3
# Author: Thit Lwin Oo
# Author ID: 170549232
# Date Created: 2025/05/20

import sys
if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer -= 1
print("blast off!")


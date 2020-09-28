#!/bin/python3

import subprocess
import os
import sys

pppid = int(os.popen("ps -p %d -oppid=" % os.getppid()).read().strip())
filename = '/tmp/sysctl_restore_%d.sh' % pppid

restore_file = open(filename, 'w')
print('#!/bin/bash', file=restore_file)

for a in sys.argv[1:]:
  sysctl = a.split('=')

  # save current value
  cur_val = subprocess.getoutput('cat ' + sysctl[0])
  print('echo "%s" > %s' % (cur_val, sysctl[0]), file=restore_file)

  # set new value
  cmd = 'echo "%s" > %s' % (sysctl[1], sysctl[0])
  os.system(cmd)

os.system('chmod u+x %s' % filename)

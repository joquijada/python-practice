import os

try:
  myCmd = os.popen('crap').read()
  print myCmd
except BaseException:
  print "Error"

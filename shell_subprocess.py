import subprocess
import sys

try:
  out = subprocess.Popen("uname", 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
  stdout,stderr = out.communicate()
  print stdout
  print "Is CYGWIN?" 
  print "CYGWIN" in stdout
  print "Error (if any) is " 
  print stderr
except Exception, e:
  print "Oh crap "
  raise

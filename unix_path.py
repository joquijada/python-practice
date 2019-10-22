import subprocess


def unixPath(path):
  try:
    out = subprocess.Popen(["cygpath", "-u", path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    return stdout
  except Exception, e:
    return path


print unixPath('C:\\foo\\bar\\blah')

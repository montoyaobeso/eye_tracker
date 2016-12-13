from subprocess import Popen, PIPE

p = Popen("MinimalGazeDataStream.exe", stdout=PIPE)

for line in iter(p.stdout.readline,""):
     print "captured:",line,
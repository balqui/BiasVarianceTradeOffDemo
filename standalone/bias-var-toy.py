# See BVT.py for an attempt to move this alive into Brython

from random import gauss

N = 25
m = 3.3
sig = 2
decs = 6

d = []
for i in range(N):
	d.append(gauss(m,sig))

s = 0
for e in d:
	print e
	s += e

for p in range(0,decs):
	form = "%%1.%df" % p
	print form % (s/len(d))



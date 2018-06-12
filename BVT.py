"""
Very simple toy demonstrating 
a very simple case of bias/variance trade-off.

Check for companion file index.html nearby.

Browser complains about coding line, removed:
# -*- coding: utf-8 -*-

"""

about_str = """Using Brython to construct a very simple toy 
demonstrating a very simple case of 
bias/variance trade-off.

Aesthetics to be taken care of some day.

José L Balcázar (balqui at BitBucket or GitHub)
2018"""

from browser import document, alert, html # Brython in-browser support
from random import gauss

def about():
	alert(about_str)

def start(event):
	"get parameter values and reinitialize data"
	mean = float(document["mean"].value)
	stdev = float(document["stdev"].value)
	ssize = int(document["ssize"].value)
	decs = 6 # max of decimal places to test

	document['approxmean'].text = ""
	document['samplevalues'].text = ""

	d = []
	for i in range(ssize):
		d.append(gauss(mean,stdev))
	s = sum(d)

#	s = 0
#	for e in d:
#		#print e
#		s += e

	for p in range(0,decs):
		form = "%%1.%df" % p
		#print form % (s/len(d))
		document['approxmean'] <= html.P(form % (s/len(d)))

	for e in d:
		document['samplevalues'] <= html.P(str(e))

# main program: 
# bind buttons to processes and leave everything for Brython to care for.

document['aboutbutton'].bind('click', about)

document['samplebutton'].bind('click', start)



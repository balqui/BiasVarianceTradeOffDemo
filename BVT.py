# -*- coding: utf-8 -*-

"""
Very simple toy demonstrating 
a very simple case of bias/variance trade-off.

Check for companion file index.html nearby.
"""

about_str = """Using Brython to construct a 
very simple toy demonstrating 
a very simple case of bias/variance trade-off.

Aesthetics to be taken care of some day.

José L Balcázar (balqui at BitBucket or GitHub), 2018"""

from browser import document, alert, html # Brython in-browser support

def about():
	alert(about_str)

def start(event):
	"get parameter values"
	mean = int(document["mean"].value)
	stdev = int(document["stdev"].value)
	ssize = int(document["ssize"].value)
	decs = 6 # max of decimal places to test

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



def extenddata():
	"add one more point and recompute the optimum clustering of the points so far"
	global i
	i += 1
	new = float(document["value"].value)
	if data:
		if data[-1] >= new:
			alert("Please provide the points in increasing order. Last input ignored.")
			i -= 1
			document['value'].value = ""
			document['value'].placeholder = "Please input value " + str(i) + " and submit it"
			return
	data.append(new)
	if len(data) < nclus:
		document['allvalues'].text = t(data)
	else:
		b = getJenksBreaks(data, nclus)
		document['allvalues'].text = t(data, b)
	if i > nval:
		"i started counting at 1"
		document['value'].disabled = True
		document['submitbutton'].disabled = True
		document['startbutton'].disabled = True
		document['newvalue'].disabled = False
		document['submitnewbutton'].disabled = False
		document['newvalue'].placeholder = "Please input one additional value and submit it"
	else:
		document['value'].value = ""
		document['value'].placeholder = "Please input value " + str(i) + " and submit it"

def go(ev):
	"actual process: compute clusterings of initial segments"
	new = float(document["newvalue"].value)
	if data[-1] >= new:
		alert("Please provide the points in increasing order. Last input ignored.")
		document['newvalue'].value = ""
		document['newvalue'].placeholder = "Please input one additional value and submit it"
		return
	document['newvalue'].disabled = True
	document['submitnewbutton'].disabled = True
	data.append(new)
	for i in range(nclus-1, len(data)):
		b = getJenksBreaks(data[:i], nclus-1)
		document['allclus'] <= html.P(t(data, b))
	b = getJenksBreaks(data, nclus)
	document['bestclus'].text = t(data, b)



# main program: 
# bind buttons to processes and leave everything for Brython to care for.

document['aboutbutton'].bind('click', about)

document['samplebutton'].bind('click', start)



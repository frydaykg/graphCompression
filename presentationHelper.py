import sys
import os
import copy
import time
import random
from CompressionAlgorythms.simpleCompressionHorizontal import *
from CompressionAlgorythms.simpleCompressionVertical import *
from CompressionAlgorythms.simpleGreedyCompression import *
import graphLoading
from CompressionAlgorythms import distCompression
from CompressionAlgorythms import modularCompression
from common import *
import normalFormProvider

def getS(m,e):
	if isinstance(e, tuple):
		a = getAllVertics(e[0])
		b = getAllVertics(e[1])
		
		if len(a) > 1 and len(b) > 1:
			nn = m + 1
			ee = [(list(a), [nn]), ([nn], list(b))]
			return (nn, ee)
		return (m, e)
	elif isinstance(e, list):
		ee = []
		for i in e:
			(mm, eee) = getS(m, i)
			ee.append(eee)
			m = mm
		return (m, ee)
	else:
		return (m, e)

def printModDecReplace(s):
	(q, c) = (s[0], s[1])
	
	print getExpressionByEdges(q)
	print
	for i in c:
		print getExpressionByEdges(i[0]) + " = " + getExpressionByEdges(i[1])

simple = True
if simple:
	n = 4
	a = []
	for i in range(n):
		a.append([0]*n)
		
	a[2][1] = a[1][2] = 1
	a[0][1] = a[2][3] = 1
else:
	(n, a) = graphLoading.loadGraph('0.edges')
	
isM = True

for i in range(len(sys.argv)):
	if sys.argv[i] == '--internal':
		isM = False
	if sys.argv[i] == '-f':
		(n, a) = graphLoading.loadGraph(sys.argv[i + 1])

if isM:
	ed = modularCompression.compress(a, n)
else:
	ed = distCompression.compress(a, n)
ed2 = getS(max(getAllVertics(ed)), ed)[1]

print '*'*20
print "NormalForm:"
print getExpressionByEdges(normalFormProvider.getNormalForm(a, n))
print

print "Compressed:"
print getExpressionByEdges(ed)
print

print "Modified:"
print getExpressionByEdges(ed2)
print '*'*20

q1 = len(getAllVertics(ed)) + countEdges(a, n)
q2 = len(getAllVertics(ed2)) + countEdges(getMatrixByEdges(ed2, len(getAllVertics(ed2))), len(getAllVertics(ed2)))

print "E + V before:", q1
print "E + V after:", q2

G = getSageGraph(getMatrixByEdges(ed, len(getAllVertics(ed))), len(getAllVertics(ed)))
P = G.plot()
P.show()

G = getSageGraph(getMatrixByEdges(ed2, len(getAllVertics(ed2))), len(getAllVertics(ed2)))
P = G.plot()
P.show()

raw_input()
exit()

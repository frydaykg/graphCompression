from CompressionAlgorythms import simpleGreedyCompression
from common import *
from sage.graphs.modular_decomposition.modular_decomposition import modular_decomposition
import time
import cProfile
import random
import graphLoading
import normalFormProvider
from CompressionAlgorythms import distCompression
from CompressionAlgorythms import modularCompression
from CompressionAlgorythms import simpleCompressionHorizontal

#random.seed(1)

n = 30
a = getRandomGraph(n)

l1 = l2 = l3 = l4 = t1 = t2 = t3 = t4 = 0

start = time.time()
distCompression.compress([])
print time.time() - start, "sec"

for i in range(50):
	a = getRandomGraph(n)
	
	start = time.time()
	ex = normalFormProvider.getNormalForm(a, n)
	t1 += time.time() - start
	l1 += expressionLen(getExpressionByEdges(ex))

	start = time.time()
	ex = distCompression.compress(simpleCompressionHorizontal.compress(a, n))
	t2 += time.time() - start
	l2 += expressionLen(getExpressionByEdges(ex))

	start = time.time()
	ex = distCompression.compress(simpleGreedyCompression.compress(a, n))
	t3 += time.time() - start
	l3 += expressionLen(getExpressionByEdges(ex))
	
	start = time.time()
	ex = modularCompression.compress(a, n)
	t4 += time.time() - start
	l4 += expressionLen(getExpressionByEdges(ex))

print "NormalForm"
print "T =", t1
print "L =", l1
print "DistCompress with Horizontal "
print "T =", t2
print "L =", l2
print "DistCompress with SimpleGreedy "
print "T =", t3
print "L =", l3
print "Modular"
print "T =", t4
print "L =", l4


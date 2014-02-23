import distCompression
from common import *
from sage.all import *
from sage.graphs.modular_decomposition.modular_decomposition import modular_decomposition

def compress(a,n):
	l = modular_decomposition(getSageGraph(a, n))
	return __compress(l, a)

def __compress(l, a):
	if isinstance(l, int):
		return l
	elif l[0] == 'Serie' or l[0] == 'Prime':
		d = []
		for i in l[1]:
			if not isinstance(i, int):
				d.append(getAnyVertex(i))
			else:
				d.append(i)
		cedges = getCompressedEdges(a, d)
		for i in range(len(l[1])):
			if not isinstance(l[1][i], int):
				compressed = __compress(l[1][i], a)
				cedges = changeVertex(cedges, d[i], compressed)
		return cedges
	else:
		return [__compress(i, a) for i in l[1]]

def compressWihReplace(a, n):
	l = modular_decomposition(getSageGraph(a, n))
	(e, c, n) = compress2sub(l, a, n)
	q = c.pop()
	return (q[1], c)
	
def compress2sub(l, a, n):
	ch = []
	if isinstance(l, int):
		return (l, ch, n)
	elif l[0] == 'Serie' or l[0] == 'Prime':
		d = []
		for i in l[1]:
			if not isinstance(i, int):
				d.append(getAnyVertex(i))
			else:
				d.append(i)		
		cedges = getCompressedEdges(a, d)
		for i in range(len(l[1])):
			if not isinstance(l[1][i], int):
				(compressed, c, n) = compress2sub(l[1][i], a, n)
				for cc in c:
					ch.append(cc)
				cedges = changeVertex(cedges, d[i], compressed)
		ch.append((n, cedges))
		return (n, ch, n+1)
	else:
		ee=[]
		for i in l[1]:
			(e, c, n) = compress2sub(i, a, n)
			for cc in c:
				ch.append(cc)
			ee.append(e)
		ch.append((n, ee))
		return (n, ch, n+1)


def changeVertex(edges, v1, v2):	
	if isinstance(edges, list):
		for i in range(len(edges)):
			edges[i] = changeVertex(edges[i], v1, v2)
		return edges
	elif isinstance(edges, tuple):
		el = []
		for i in range(len(edges)):
			el.append(changeVertex(edges[i], v1, v2))
		return tuple(el)
	elif edges == v1:
		return v2
	return edges

def getAnyVertex(l):
	while not isinstance(l[1][0], int):
		l = l[1][0]
	return l[1][0]
	
def getCompressedEdges(a,d):
	vertics = getSingleVertics(a, d)
	edges = getEdgesHorizontal(a, d)
	return distCompression.compress(edges + vertics)
		
def getSingleVertics(a, d):
	vertics = []
	for i in d:
		k = 0
		for j in d:
			k += a[i][j]
			k += a[j][i]
		if k == 0:
			vertics.append(i)
	return vertics

def getEdgesHorizontal(a,d):
	edges = []
	for i in d:	
		k = 0
		for j in d:
			k += a[i][j]
		if k != 0:
			intlist = []
			for j in d:
				if a[i][j] == 1:
					intlist.append(j)
			edges.append(([i],intlist))
	return edges

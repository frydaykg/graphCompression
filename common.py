import random as sysrandom
import sys
from sage.all import *

def expressionLen(s):
	return s.count('+') + s.count('->') + 1

def deleteNonsignificantBrakes(s):
	pos = range(len(s))
	for i in range(len(s) - 2):
		if s[i] == '(' and s[i + 2] == ')':
			pos.remove(i)
			pos.remove(i + 2)
	return "".join([s[i] for i in pos])

def letByInt(i):
	if i == 0:
		return 'a'
	result = ''
	while i != 0:
		result = chr(i%26 + ord('a')) + result
		i = int(i/26)
	return result

def column(matrix, i):
	return [row[i] for row in matrix]

def getMatrixByEdges(edges, n):
	a = []
	for i in range(n):
		a.append([0] * n)
	for edge in edges:
		links = getLinks(edge)
		for link in links:
			a[link[0]][link[1]] = 1
	return a

def getLinks(edge):
	links = []
	if isinstance(edge, tuple):
		if len(edge) != 2:
			5/0
		for i in getAllVertics(edge[0]):
			for j in getAllVertics(edge[1]):
				links.append((i, j))
		for i in getLinks(edge[0]):
			links.append(i)
		for i in getLinks(edge[1]):
			links.append(i)
	if isinstance(edge, list):
		for i in edge:
			for j in getLinks(i):
				links.append(j)
	return links

def getAllVertics(edge):
	l = set()
	if isinstance(edge, (tuple,list)):
		for i in edge:
			ll = getAllVertics(i)
			if isinstance(ll, set):
				for j in ll:
					l.add(j)
			else:
				l.add(ll)
		return l
	else:
		return edge

def isMatrixEquals(a, b, n):
	for i in range(n):
		for j in range(n):
			if a[i][j] != b[i][j]:
				return False
	return True

def getExpressionByEdges(edges):
	if isinstance(edges, int):
		return letByInt(edges)
	ads = []
	for edge in edges:
		ads.append(getAds(edge))
	s = '+'.join(ads)
	return deleteNonsignificantBrakes(s)

def getAds(edge):
	if isinstance(edge, tuple):
		return '(' + getAds(edge[0]) + ')->(' + getAds(edge[1]) + ')'
	elif isinstance(edge, list):
		return '+'.join([getAds(i) for i in edge])
	else:	
		return str(letByInt(edge))

def countEdges(a,n):
	k = 0
	for i in range(n):
		for j in range(n):
			if a[i][j] == 1:
				k += 1
	return k

def getRandomGraph(n):
	a=[]
	for i in range(n):
		a.append([0] * n)
	edg = sysrandom.randint(0, n*n - n)
	k = 0
	while k != edg:
		i = sysrandom.randint(0, n-1)
		j = sysrandom.randint(0, n-1)
		if a[i][j] != 1 and i != j:
			a[i][j] = 1
			k += 1
	return a

def getCompleteGraph(n):
	a = []
	for i in range(n):
		a.append([1] * n)

	for i in range(n):
		a[i][i] = 0
	return a

def getTournirGraph(n):
	a = []
	for i in range(n):
		a.append([0] * n)
	for i in range(n - 1):
		for j in range(i + 1, n):
			a[i][j] = 1
	return a

def getRandomGraph(n,v):
	a = []
	for i in range(n):
		a.append([0] * n)
	k = 0
	while k != v:
		i = sysrandom.randint(0, n-1)
		j = sysrandom.randint(0, n-1)
		if a[i][j] != 1 and i != j:
			a[i][j] = 1
			k += 1
	return a

def getCellGraph(n):
	nn = n * n
	a = []
	for i in range(nn):
		a.append([0] * nn)

	for i in range(n):
		for j in range(n-1):
			x = i*n + j
			y = x + 1
			a[x][y] = 1
			a[y][x] = 1

			x = j*n + i
			y = x + n
			a[x][y] = 1
			a[y][x] = 1
	return a

def getSageGraph(a, n):
	g = DiGraph()
	for i in range(n):
		g.add_vertex()
	
	for i in range(n):
		for j in range(n):
			if a[i][j] == 1:
				g.add_edge(i, j)
	return g

def getClicksGraph(l):
	n = sum(l)
	
	a = []
	for i in range(n):
		a.append([0] * n)
	
	k = 0
	for kk in l:
		for i in range(k, k + kk):
			for j in range(k, k + kk):
				if i != j:
					a[i][j] = 1
		k += kk
	
	k=0
	for i in range(len(l) - 1):
		a[k][k + l[i]] = 1
		k += l[i]
	return a
		

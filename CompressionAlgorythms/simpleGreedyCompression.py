from copy import deepcopy
from common import *

def countColumns(a, n):
	q = []
	for i in xrange(n):
		q.append(0)
		for j in xrange(n):
			if a[j][i] == 1:
				q[-1] += 1
	return q

def compress(a,n):
	a = deepcopy(a)
	summands = []
	symbolUsed = [False] * n
	
	while True:
		hCount = [a[i].count(1) for i in range(n)]
		vCount = countColumns(a, n)
		hMax = max(hCount)
		vMax = max(vCount)
		
		if hMax == 0:
			break
		
		intList = []
		if hMax >= vMax:
			i = hCount.index(hMax)
			symbolUsed[i] = True
			for j in range(n):
				if a[i][j] == 1:
					a[i][j] = 0
					symbolUsed[j] = True
					intList.append(j)
			summands.append((i, intList))
		else:
			i = vCount.index(vMax)
			symbolUsed[i] = True
			for j in range(n):
				if a[j][i] == 1:
					a[j][i] = 0
					symbolUsed[j] = True
					intList.append(j)
			summands.append((intList, i))

	for i in range(n):
		if symbolUsed[i] == False:
			summands.append(i)
	return summands

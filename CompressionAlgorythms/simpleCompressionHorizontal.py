from common import *

def compress(a, n):
	summands = []
	for i in range(n):	
		if a[i].count(1) == 0:
			if column(a,i).count(1) == 0:
				summands.append(i)
		else:
			intlist = []
			for j in range(n):
				if a[i][j] == 1:
					intlist.append(j)
			summands.append((i, intlist))
	return summands

from common import *

def simpleCompressionVertical(a,n):
	summands = []
	for i in range(n):	
		if column(a,i).count(1) == 0:
			if a[i].count(1) == 0:
				summands.append(i)
		else:
			intlist = []
			for j in range(n):
				if a[j][i] == 1:
					intlist.append(j)
			summands.append((intlist, i))
	return summands

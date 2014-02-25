def getNormalForm(a, n):
	edges = getEdgesNormal(a, n)
	singleVertics = getSingleVertics(a, n)
	return edges + singleVertics

def getEdgesNormal(a,n):
	edges = []
	for i in range(n):
		for j in range(n):
			if a[i][j] == 1:
				edges.append(([i], [j]))
	return edges

def getSingleVertics(a, n):
	vertics = []
	for i in range(n):
		for j in range(n):
			if a[i][j] == 0 and a[j][i] == 0: 
				break
		else:
			vertics.append(i)
	return vertics


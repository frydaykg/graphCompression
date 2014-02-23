import string

def loadGraph(filename):
	f = open(filename,'r')
	lines = f.readlines()
	maxV = 0
	for line in lines:
		(a, b) = map(int, string.split(line, ' '))
		maxV = max(maxV, max(a, b))
	maxV += 1
	res = []
	for i in range(maxV):
		res.append([0] * maxV)

	for line in lines:
		(a, b) = map(int, string.split(line, ' '))
		res[a][b]=1
	return (maxV, res)


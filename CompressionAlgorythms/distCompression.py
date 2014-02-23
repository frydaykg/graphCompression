import normalFormProvider

def prepare(ex):
	edges = []
	for e in ex:		
		if isinstance(e, tuple):
			a = e[0]
			b = e[1]
			if not isinstance(a, list):
				a = [a]
			if not isinstance(b, list):
				b = [b]
			edges.append((a, b))
		else:
			edges.append(e)
	return edges


def compress(ex):
	done = False
	
	edges = prepare(ex)
	
	while not done:
		n=len(edges)
		for i in range(n-1):
			if not isinstance(edges[i], (list, tuple)):
				continue
			for j in range(i+1,n):
				if not isinstance(edges[j], (list, tuple)):
					continue
				R = getR(edges[i],edges[j])
				if len(R) > 0:
					I = getI(edges[i], edges[j])
					N1 = getN1(edges[i], edges[j])
					N2 = getN2(edges[i], edges[j])
					M1 = getM1(edges[i], edges[j])
					M2 = getM2(edges[i], edges[j])
					(res, type) = check(R, I, N1, N2, M1, M2)
					if res:
						do(edges,i,j,type,R,I,N1,N2,M1,M2)
						done=True
						break
				  
				I = getI(edges[i], edges[j])
				if len(I) > 0:
					N1=getN1(edges[i],edges[j])
					N2=getN2(edges[i],edges[j])
					M1=getM1(edges[i],edges[j])
					M2=getM2(edges[i],edges[j])
					(res, type) = check(R, I, N1, N2, M1, M2)
					if res:
						do(edges,i,j,type,R,I,N1,N2,M1,M2)
						done=True
						break
			if done:
				break
		if done:
			done=False
		else:
			break
	return edges


def do(edges,i,j,type,R,I,N1,N2,M1,M2):
	#(R,I,N1,N2,M1,M2) =map(list,(R,I,N1,N2,M1,M2))
	(Rl,Il,N1l,N2l,M1l,M2l) =map(len,(R,I,N1,N2,M1,M2))
	edges.pop(min(i,j))
	edges.pop(max(i,j)-1)
	if type ==0:
		if Rl+N1l+N2l>0 and Il>0:
			edges.append((R+N1+N2,I))
		if Rl+N1l>0 and M1l>0:
			edges.append((R+N1,M1))
		if Rl+N2l>0 and M2l>0:
			edges.append((R+N2,M2))
	elif type ==1:
		if Rl+N1l+N2l>0 and Il>0:
			edges.append((R+N1+N2,I))
		if N1l>0 and M1l>0:
			edges.append((N1,M1))
		if N2l>0 and M2l>0:
			edges.append((N2,M2))
		if M1l+M2l>0 and Rl>0:
			edges.append((R,M1+M2))
	elif type ==2:
		if Il+M1l+M2l>0 and Rl>0:
			edges.append((R,I+M1+M2))
		if Il+M1l>0 and N1l>0:
			edges.append((N1,I+M1))
		if Il+M2l>0 and N2l>0:
			edges.append((N2,I+M2))
	else:
		if Il+M1l+M2l>0 and Rl>0:
			edges.append((R,I+M1+M2))
		if N1l>0 and M1l>0:
			edges.append((N1,M1))
		if N2l>0 and M2l>0:
			edges.append((N2,M2))
		if N1l+N2l>0 and Il>0:
			edges.append((N1+N2,I))


def check(R,I,N1,N2,M1,M2):
	(R,I,N1,N2,M1,M2) = map(len,(R,I,N1,N2,M1,M2))
	A = R*2 + I*2 + N1 + N2 + M1 + M2

	N = N1 + N2
	M = M1 + M2


	ri=1 if R>0 else 0
	ii=1 if I>0 else 0
	n1i=1 if N1>0 else 0
	n2i=1 if N2>0 else 0
	m1i=1 if M1>0 else 0
	m2i=1 if M2>0 else 0
	mi=1 if M>0 else 0
	ni=1 if N>0 else 0

	a11=0
	if R+N>0 and I>0:
		a11=R+I+N
	a12=0
	if I+M>0 and R>0:
		a12=R+I+M

	temp = (N1 + M1)*n1i*m1i + (N2 + M2)*n2i*m2i
	
	a211=0
	if R+N1>0 and M1>0:
		a211 += R + N1 + M1
	if R+N2>0 and M2>0:
		a211 += R + N2 + M2
	a212 = temp + (R + M)*ri*mi

	a221=0
	if I+M1>0 and N1>0:
		a221 += I + N1 + M1
	if I+M2>0 and N2>0:
		a221 += I + N2 + M2
	a222 = temp + (I + N)*ii*ni

	"""???? ??? ???? ???????????? ? ?????? ?????? ? ????????? ?????? ??? ?????????? ??????? ?????"""
	am1 = a11 + a211
	am2 = a11 + a212
	am3 = a12 + a221
	am4 = a12 + a222	
	m = min(min(am1, am2), min(am3, am4))
	if A - m <= 0:
		return(False, -1)
	
	mins = [am1, am2, am3, am4]
	type = mins.index(m)
	return (True, type)


def getR(a, b):	
	return [x for x in a[0] if x in b[0]]

def getI(a,b):
	return [x for x in a[1] if x in b[1]]

def getNM(a,b,k):
	return [x for x in a[k] if x not in b[k]]

def getN1(a,b):
	return getNM(a,b,0)

def getN2(a,b):
	return getNM(b,a,0)

def getM1(a,b):
	return getNM(a,b,1)

def getM2(a,b):
	return getNM(b,a,1)

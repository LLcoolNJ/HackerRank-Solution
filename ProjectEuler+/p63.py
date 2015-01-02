from math import floor,ceil
def getfir(n):
	a = pow(10,n-1)
	return (int(ceil(pow(a,1/float(n)))),int(floor(pow(a*10 -1,1/float(n)))))
n = input()
fir,las = getfir(n)
while fir <= las:
	print pow(fir,n)
	fir += 1
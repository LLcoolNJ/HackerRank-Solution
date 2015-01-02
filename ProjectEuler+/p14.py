p = [1, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235, 313, 327, 649, 654, 655, 667, 703, 871, 1161, 2223, 2322, 2323, 2463, 2919, 3711, 6171, 10971, 13255, 17647, 17673, 23529, 26623, 34239, 35497, 35655, 52527, 77031, 106239, 142587, 156159, 216367, 230631, 410011, 511935, 626331, 837799, 1117065, 1126015, 1501353, 1564063, 1723519, 2298025, 3064033, 3542887, 3732423]
n = []
for i in xrange(input()):
	n.append(input())
l = len(p)
c = 0
for i in n:
	for j in xrange(l):
		if i>= 3732423:
			print 3732423
			break
		if i < p[j]:
			c = 1
			print p[j-1]
			break
'''
import time
def c(n,i):
	if n%2==0:
		n /= 2
	else:
		n = 3*n+1
	if n==1:
		return i
	else: return c(n,i+1)
n = []
t = input()
s = time.time()
for i in xrange(1,t+1):
	n.append(c(i,1))
print len(n)
for i in n:
	c(i,1)
print time.time()-s
'''
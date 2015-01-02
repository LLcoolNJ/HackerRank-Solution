from fractions import gcd
class frac:
	def __init__(self,num,den=1):
		self.num = num
		self.den = den
	def add(self,f):
		self.num = self.num*f.den + f.num*self.den
		self.den *= f.den
		# l = gcd(self.num,self.den)
		# self.num /= l
		# self.den /= l
	def rec(self):
		self.num,self.den = self.den,self.num
def getEle(n):
    q,r = divmod(n,3)
    if r == 0:
        return q*2
    return 1
n = input()
if n == 1:
	print 2
else:
	f = frac(getEle(n))
	for i in xrange(n-1,1,-1):
		#print f,getEle(i)
		f.rec()
		f.add(frac(getEle(i)))
		# f = 1/f + getEle(i)
	f.rec()
	f.add(frac(2))
	# f = 1/f + 
	num = f.num
	den = f.den
	l = gcd(num,den)
	num /= l
	st = str(num)
	print sum(map(int,st))
	# for i in st:
		# s += int(i)
	# print s
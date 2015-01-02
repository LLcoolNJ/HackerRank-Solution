from fractions import gcd
class frac:
	def __init__(self,num,den=1):
		self.num = num
		self.den = den
	def add(self,f):
		self.num = self.num*f.den + f.num*self.den
		self.den *= f.den
		l = gcd(self.num,self.den)
		self.num /= l
		self.den /= l
	def addg(self,f):
		l = (f.den*self.den)/gcd(f.den,self.den)
		self.num = self.num*(l/self.den) + f.num*(l/f.den)
		self.den = l
	def rec(self):
		self.num,self.den = self.den,self.num
n = input()
f = frac(3,2)
for i in xrange(1,n):
	f.addg(frac(1))
	f.rec()
	f.addg(frac(1))
	# print f.num,f.den
	if len(str(f.num)) > len(str(f.den)) and i+1 <= n:
		print i+1
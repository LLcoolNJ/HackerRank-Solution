import time
digits = "0123456789abcdefghijklmnopqrstuvwxyz"
def baseN(num,b):
  if num == 0: return "0"
  result = ""
  while num != 0:
    num, d = divmod(num, b)
    result += digits[d]
  return result[::-1] 
def getRev(n):
	return str(n)[::-1]
	
def c(n,k):
	i=s=0
	while i<=n:
		j = str(i)
		b = baseN(i,k)
		#print j,b,getRev(j),getRev(b)
		if j == getRev(j) and str(b) == getRev(b):
			s+= i
		i += 1
	return s
n,k = map(int,raw_input().split())
print c(n,k)
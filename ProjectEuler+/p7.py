import math
def is_prime(n):
	if n == 2:
		return True
	if n == 3:
		return True
	if n%2==0:
		return False
	for i in range(3,int(math.sqrt(n))+1,2):
		if n%i == 0:
			return False
	return True
n = []
for i in range(input()):
    n.append(input())
l = max(n)
a = []
i = 2
while len(a) < l:
	if is_prime(i):
		a.append(i)
	i += 1
for i in n:
    print a[i-1]
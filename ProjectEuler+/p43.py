from itertools import permutations as P
def gen(n):
	val = 0
	s = '0123456789'
	sn = s[:n+1]
	for i in P(sn):
		k = ''.join(i)
		if ch(k):
			val += int(k)
	return val
def ch(n):
	fl = False
	if len(n) >= 4:
		if int(n[1:4])%2 == 0:
			fl = True
		else: return False
	if len(n) >= 5:
		if int(n[2:5])%3 == 0:
			fl = True
		else: return False
	if len(n) >= 6:
		if int(n[3:6])%5 == 0:
			fl = True
		else: return False
	if len(n) >= 7:
		if int(n[4:7])%7 == 0:
			fl = True
		else: return False
	if len(n) >= 8:
		if int(n[5:8])%11 == 0:
			fl = True
		else: return False
	if len(n) >= 9:
		if int(n[6:9])%13 == 0:
			fl = True
		else: return False
	if len(n) >= 10:
		if int(n[7:])%17 == 0:
			fl = True
		else: return False
	if fl:
		return True
	else:
		return False
n = input()
print gen(n)
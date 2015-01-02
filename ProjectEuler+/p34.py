l = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def is_fac(n):
	s = str(n)
	sm = 0
	for i in s:
		sm += l[int(i)]
	if sm%n == 0:
		return True
	return False
i = 10
end = input()
c = 0
while i<= end:
	if is_fac(i): c+= i
	i += 1
print c
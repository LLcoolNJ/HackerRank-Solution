def maxx(table):
	for row in range(len(table)-1, 0, -1):
		for col in range(0, row):
			table[row-1][col] += max(table[row][col], table[row][col+1])
	return table[0][0]
for i in xrange(input()):
	n = []
	for j in xrange(input()):
		n.append(map(int,raw_input().split()))
	print maxx(n)
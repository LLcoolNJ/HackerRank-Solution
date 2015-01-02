mod = 10**9+7
coins = [1, 2, 5, 10, 20, 50, 100, 200]
def c(target):
	ways = [1] + [0]*target
	for coin in coins:
		for i in range(coin, target+1):
			ways[i] += ways[i-coin]%mod
	return ways
n =[]
for i in xrange(input()):
	n.append(input())
way = c(max(n))
for i in n:
	print way[i]%mod
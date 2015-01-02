def num_prod(n,k):
	print max([reduce(lambda accum, x : accum * x, [int(x) for x in n[i:i+k]]) for i in range(len(n) - k)])
n = []
num = []
t = input()
for i in range(t):
    n.append(map(int,raw_input().split()))
    num.append(raw_input())
for i in range(t):
    num_prod(num[i],n[i][1])
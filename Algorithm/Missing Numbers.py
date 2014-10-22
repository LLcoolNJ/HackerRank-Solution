def main():
	i = 0
	j = 0
	oup = []
	size1 = input()
	inp1 = raw_input()
	inp1 = inp1.split()
	size2 = input()
	inp2 = raw_input()
	inp2 = inp2.split()
	p = list(set(inp1))
	for i in p:
		if inp1.count(i) != inp2.count(i):
			oup.append(i)
	oup = map(int,oup)
	oup = list(set(oup))
	oup = sorted(oup)
	for i in oup:
		print i,
	
if __name__ == '__main__':
	main() 

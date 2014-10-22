def main():
	t = input()
	oup = []
	for i in range(t):
		w = input()
		if w <= 2:
			oup.append(-1)
		elif w % 2 == 1:
			oup.append(2)
		elif w % 2 == 0:
			p = w/2
			if p % 2 == 0:
				oup.append(3)
			else:
				oup.append(4)
	for i in oup:
		print i
	
if __name__ == '__main__':
	main()

def main():
	t = input()
	oup = {}
	for i in range(t):
		w = input()
		oup[i] = (w*(w-1))/2
	for i in oup.values():
		print i 
		
if __name__ == '__main__':
	main()

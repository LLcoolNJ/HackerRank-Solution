def main():
	t = input()
	w = {}
	for i in range(t):
		w[i] = raw_input()
		if '-' in w[i]:
			w[i] = w[i].split('-')
		else:
			w[i] = w[i].split()
	for i in range(t):
		print 'CountryCode='+w[i][0]+',LocalAreaCode='+w[i][1]+',Number='+w[i][2]
			 
	
if __name__ == '__main__':
	main() 

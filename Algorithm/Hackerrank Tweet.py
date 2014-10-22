def main():
	t = input()
	count = 0	
	for i in range(t):
		w = raw_input()
		w = w.lower()
		if 'hackerrank' in w:
			count += 1
	print count
	
if __name__ == '__main__':
	main() 

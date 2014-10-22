def main():
	t = input()
	if t%2 == 1:
		w = raw_input()
		w = w.split()
		p = list(set(w))
	for i in p:
		if w.count(i) == 1:
			print i
			break
		
if __name__ == '__main__':
	main() 

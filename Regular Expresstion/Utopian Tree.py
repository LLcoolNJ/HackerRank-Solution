def calc(cycle):
	ht = 1
	ses = 'mon'
	while cycle > 0:
		if ses == 'mon':
			ht = 2*ht
			ses = 'somm'
		else:
			ht += 1
			ses = 'mon'
		cycle -= 1
	print ht

def main():
	t = input()
	no = []
	for i in range(t):
		w = input()
		no.append(w)
	for i in no:
		calc(i)
	
if __name__ == '__main__':
	main()
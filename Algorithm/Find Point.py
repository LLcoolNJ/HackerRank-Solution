def main():
	t = input()
	w = {}
	p = {}
	for i in range(t):
		w[i] = raw_input()
		w[i] = w[i].split()
		w[i] = map(int,w[i])
		x = w[i][2] + w[i][2] - w[i][0]
		y = w[i][3] + w[i][3] - w[i][1]
		p[i] = (str)(x) + ' '+ (str)(y)
	for i in p.values():
		print i
	
if __name__ == '__main__':
	main() 
import re
def main():
	t = input()
	w = {}
	oup = []
	for i in range(t):
		w[i] = raw_input()
		if re.findall('\w+\.\w+@\w+\.\w+\.\w+',w[i]):
			oup += re.findall('\w+\.\w+@\w+\.\w+\.\w+',w[i])
		elif re.findall('\w+@\w+\.\w+\.\w+\.\w+',w[i]):
			oup += re.findall('\w+@\w+\.\w+\.\w+\.\w+',w[i])
		elif re.findall('\w+@\w+\.\w+\.\w+',w[i]):
			oup += re.findall('\w+@\w+\.\w+\.\w+',w[i])
		elif re.findall('\w+@\w+\.\w+',w[i]):
			oup += re.findall('\w+@\w+\.\w+',w[i])
	oup = list(set(oup))
	oup.sort()
	p = ';'.join(oup)
	print p

if __name__ == '__main__':
	main() 

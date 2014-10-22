import re
def main():
	p = input()
	t = 'YES'
	f = 'NO'
	oup = []
	for i in range(p):
		w = raw_input()
		if len(w) == 10:
			if re.match('[A-Z]{5}[0-9]{4}[A-Z]',w):
				oup.append(t)
			else:
				oup.append(f)
		else:
			oup.append(f)
	for i in oup:
		print i
	
if __name__ =='__main__':
	main()

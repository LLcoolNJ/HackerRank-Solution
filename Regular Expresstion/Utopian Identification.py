import re

def main():
	p = input()
	t = 'VALID'
	f = 'INVALID'
	oup = []
	for i in range(p):
		w = raw_input()
		if re.match('[a-z]{0,3}\d{2,8}[A-z]{3,}',w):
			oup.append(t)
		else:
			oup.append(f)
	for i in oup:
		print i
	
if __name__ == '__main__':
	main() 

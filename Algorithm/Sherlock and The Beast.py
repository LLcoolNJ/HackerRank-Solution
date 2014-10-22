def cal(num):
	f = 5
	t = num - 5
	while t >= 3:
		if f % 5 == 0 and t % 3 == 0:
			a = (t,f)
			return a
		else:
			t -= 5
			f += 5
	return False
	
def evil(num):
	oup = 0
	if num > 2 and num % 3 == 0:
		q = num/3
		if q >= 10:
			p = q/10
			r = q%10
			oup = 555555555555555555555555555555
			for i in range(1,p):
				oup = oup*1000000000000000000000000000000 + 555555555555555555555555555555
			for i in range(r):
				oup = oup*1000 + 555
		elif q >= 5:
			p = q/5
			r = q%5
			oup = 555555555555555
			for i in range(1,p):
				oup = oup*1000000000000000 + 555555555555555
			for i in range(r):
				oup = oup*1000 + 555
		else:
			oup = 555
			for i in range(1,q):
				oup = oup*1000 + 555
	elif num < 20 and num % 5 == 0:
		q = num/5
		if q >= 10:
			p = q/10
			r = q%10
			oup = 33333333333333333333333333333333333333333333333333
			for i in range(1,p):
				oup = oup*100000000000000000000000000000000000000000000000000 + 33333333333333333333333333333333333333333333333333
			for i in range(r):
				oup = oup*100000 + 33333
		elif q>=5:
			p = q/5
			r = q%5
			oup = 3333333333333333333333333
			for i in range(1,p):
				oup = oup*10000000000000000000000000 + 3333333333333333333333333
			for i in range(r):
				oup = oup*100000 + 33333
		else:
			oup = 33333
			for i in range(1,q):
				oup = oup*100000 + 33333
	elif num > 2:
		b = cal(num)
		if b:
			q1 = b[0]/3
			q2 = b[1]/5
			if q1 >= 10:
				p1 = q1/10
				r1 = q1%10
				oup = 555555555555555555555555555555
				for i in range(1,p1):
					oup = oup*1000000000000000000000000000000 + 555555555555555555555555555555
				for i in range(r1):
					oup = oup*1000 + 555
			elif q1>=5:
				p1 = q1/5
				r1 = q1%5
				oup = 555555555555555
				for i in range(1,p1):
					oup = oup*1000000000000000 + 555555555555555
				for i in range(r1):
					oup = oup*1000 + 555
			else:
				oup = 555
				for i in range(1,q1):
					oup = oup*1000 + 555
			if q2 >= 10:
				p2 = q2/10
				r2 = q2%10
				for i in range(p2):
					oup = oup*100000000000000000000000000000000000000000000000000 + 33333333333333333333333333333333333333333333333333
				for i in range(r2):
					oup = oup*100000 + 33333
			elif q2>=5:
				p2 = q2/5
				r2 = q2%5
				for i in range(p2):
					oup = oup*10000000000000000000000000 + 3333333333333333333333333
				for i in range(r2):
					oup = oup*100000 + 33333
			else:
				for i in range(q2):
					oup = oup*100000 + 33333
		else:
			oup = -1
	else:
		oup = -1
	print oup

def main():
	t = input()
	inp = []
	for i in range(t):
		w = input()
		inp.append(w)
	for i in range(t):
		evil(inp[i])
	
if __name__ == '__main__':
	main() 
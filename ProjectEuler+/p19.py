import math
mon = {1:11,2:12,3:1,4:2,5:3,6:4,7:5,8:6,9:7,10:8,11:9,12:10}
def day_sun(m,y):
	#m = (m-2)%12
	m = mon[m]
	if m > 10: y -= 1
	#print m,y
	if (1 + int(math.floor(2.6*m - 0.2)) + 5*(y%4) + 4*(y%100) + 6*(y%400))%7 == 0:
		#print m,y
		return True
	else:
		return False
def iter(yr1,yr2):
	d1,m1,y1 = yr1[2],yr1[1],yr1[0]
	d2,m2,y2 = yr2[2],yr2[1],yr2[0]
	cnt = 0
	if d1 > 1:
		if m1 != 12: m1 += 1
		else:
			m1 = 1
			y1 += 1
	for y in xrange(y1,y2+1):
		mn = 1
		mj = 13
		if y == y1: mn = m1
		if y == y2: mj = m2 +1 
		for m in xrange(mn,mj):
			if day_sun(m,y):
				cnt += 1
	return cnt
for i in xrange(input()):
	y1 = map(int,raw_input().split())
	y2 = map(int,raw_input().split())
	print iter(y1,y2)
import math
def pr(n):
	lim=n
	sqrtlim=math.sqrt(float(lim))
	pp=2
	ss=[pp]
	ep=[pp]
	pp+=1
	rss=[ss[0]]
	tp=[pp]
	i=0
	rss.append(rss[i]*tp[0])
	xp=[]
	pp+=ss[0]
	npp=pp
	tp.append(npp)
	while npp<int(lim):
		i+=1
		while npp<rss[i]+1:
			for n in ss:
				npp=pp+n
				if npp>int(lim): break
				if npp<=rss[i]+1: pp=npp
				sqrtnpp=math.sqrt(npp)
				test=True
				for q in tp:
					if sqrtnpp<q: break
					elif npp%q==0:
						test=False
						break
				if test:
					if npp<=sqrtlim: tp.append(npp)
					else: xp.append(npp)
			if npp>int(lim): break
		if npp>int(lim): break
		lrpp=pp
		nss=[]
		while pp<(rss[i]+1)*2-1:
			for n in ss:
				npp=pp+n
				if npp>int(lim): break
				sqrtnpp=math.sqrt(npp)
				test=True
				for q in tp:
					if sqrtnpp<q: break
					elif npp%q==0:
						test=False
						break
				if test:
					if npp<=sqrtlim: tp.append(npp)
					else: xp.append(npp)
				if npp%tp[0]!=0:
					nss.append(npp-lrpp)
					lrpp=npp
				pp=npp
			if npp>int(lim): break
		if npp>int(lim): break
		ss=nss
		ep.append(tp[0])
		del tp[0]
		rss.append(rss[i]*tp[0])
		npp=lrpp
	ep.reverse()
	[tp.insert(0,a) for a in ep]
	tp.reverse()
	[xp.insert(0,a) for a in tp]
	return xp
	
n = []
t = input()
for i in xrange(t):
	n.append(input())
a = pr(max(n))
l = len(a)
m = max(n)
p = {}
s = 0
li = sorted(list(set(n)))
t = len(li)
j = 0
g = -1
i = 0
while i<l:
	if a[i]>li[j]:
		p[li[j]] = s
		j += 1
		continue
	s += a[i]
	i += 1
for i in xrange(j,t):
	p[li[i]] = s

for i in n:
	print p[i]

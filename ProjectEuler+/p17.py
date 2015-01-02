num = {'1':'One', '2':'Two', '3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen','19':'Nineteen','20':'Twenty','30':'Thirty','40':'Forty','50':'Fifty','60':'Sixty','70':'Seventy','80':'Eighty','90':'Ninety'}
def n2l(n):
	'''t = 'thousand'''
	h = 'Hundred'
	sn = str(n)
	'''if len(sn) == 4:
		if sn[1:] == '000':
			return num[sn[0]] + ' ' + t
		else:
			rst = num[sn[0]] + ' ' + t + ' '
			n = int(sn[1:])
			return rst + n2l(n)'''
	if len(sn) == 3:
		if sn[1:] == '00':
			return num[sn[0]] + ' ' + h + ' '
		else:
			rst = num[sn[0]] + ' ' + h + ' '
			n = int(sn[1:])
			return rst + n2l(n)
	elif len(sn) == 2:
		if sn in num:
			return num[sn]
		else:
			j = str(sn[0]) + '0'
			rst = num[j] + ' '
			return rst + n2l(n%10)
	elif len(sn) == 1 and sn != '0':
		return num[sn]
	return ''

def j(n):
	s = ''
	m = ''
	b = ''
	t = ''
	h = ''
	h = n2l(n%1000)
	n /= 1000
	t = n2l(n%1000)
	n /= 1000
	if t: t += ' Thousand ' + h
	else: t = h
	m = n2l(n%1000)
	n /= 1000
	if m: m += ' Million ' + t
	else: m = t
	b = n2l(n%1000)
	n /= 1000
	if b: b += ' Billion ' + m
	else: b = m
	print b

for i in xrange(input()):
	n = input()
	if n == 0:
		print 'Zero'
	elif n == 1000000000000:
		print 'One Trillion'
	else:
		j(n)
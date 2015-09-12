def max_profit(stocks):
	lo = stocks[0]
	maxD = 0
	for p in stocks:
		if maxD < p - lo:
			print 'maxD ' + str(maxD)
			maxD = p -lo
		if p < lo:
			print 'min ' + str(lo)
			lo = p
	return maxD

def multiplication(numbers):
	l = numbers[:]
	l2 = numbers[:]
	m = 1
	l[0] = 1
	for i,v in enumerate(numbers):
		if i != 0:
			l[i] = m*numbers[i-1]
			m = l[i]
	l2[3] = 1 
	g = 1
	for i,v in reversed(list(enumerate(numbers))):
		if i != 3:
			l2[i] = g*numbers[i+1]
			g = l2[i]
	return [a*b for a,b in zip(l,l2)]

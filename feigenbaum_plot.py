#Ben Boggs
#plots logistic map (bifurcation diagram) y=f, x=lambda

import numpy
import matplotlib.pyplot as plt

accuracy = 1000.0 #accurate to xth decimal, ie 1000.0 = accurate to thousandths
				  #lower accuracy renders faster, less sharp
				  #must be type float/double
density = 4000 #number of linearly spaced lambda values
			   #lower density renders faster, less detail
			   #must be type int

lam = numpy.linspace(0, 4, density)
x = .5 #initial population constant, arbitrary

def pattern(r, iter):
	for x in range(len(r)):
		if iter == r[x]:
			return x
	return -1


for l in lam:
	print l #completion status (done at 4.0)
	r = []
	if l<=1.00000000000:
		plt.plot(l, 0, ',r')
	else:
		r.append(0.0)
		q = l*x*(1-x)
		dq = (int(q*accuracy))/accuracy
		while pattern(r, dq) == -1:
			r.append(dq)
			q = l*r[-1]*(1-r[-1])
			dq = (int(q*accuracy))/accuracy
		for i in range(pattern(r, dq), len(r)):
			plt.plot(l, r[i], ',r')

plt.show()

'''
1: define parameters of lambda to be 0:4 in increments of .01
2: for every l in lambda:
	a. iterate to stability
		aa. as long as iterating generates new numbers, iterate
	b. plot all stability points wrt l
'''

#Ben Boggs
#trying to create a plot of logistic map (bifurcation diagram)


import numpy
import matplotlib.pyplot as plt

lam = numpy.linspace(0, 4, 400)

x = .5 #numpy.linspace(0, 1, 100)

def pattern(r, iter):
	for x in range(len(r)):
		if iter == r[x]:
			return x
	return -1


for l in lam:
	r = []
	if l<1.01:
		plt.plot(l, 0, ',r')
	else:
		r.append(0.0)
		q = l*x*(1-x)
		dq = (int(q*100000))/100000.0
		while pattern(r, dq) == -1:
			r.append(dq)
			q = l*r[-1]*(1-r[-1])
			dq = (int(q*100000))/100000.0
			print dq
		print pattern(r, dq)
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

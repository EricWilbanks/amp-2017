import numpy as np
from scipy.optimize import minimize
from scipy.optimize import fmin_slsqp

def main():
	#x[0] = x
	#x[1] = y
	#x[2] = z
	#x[3] = alpha
	#x[4] = beta

	c = 0.000001

	def objective(x):
		return x[0] * x[1] * x[2]

	def con1(x):
		return x[0] - 2*x[3]*x[1] - c

	def con2(x):
		return -x[3]*x[1]  + 5*x[4]*x[2] - c 

	def con3(x):
		return 2*x[3]*x[1] - c

	def con4(x):
		return 3*x[3]*x[1] + x[4]*x[2] - c

	def con5(x):
		return x[0] - 4*x[3]*x[1] - x[4]*x[2] - c

	def con6(x):
		return -3*x[3]*x[1] + 3*x[4]*x[2] - c

	def con7(x):
		return x[0] - 1 - c 

	def con8(x):
		return x[1] - 1 - c 

	def con9(x):
		return x[2] - 1 - c

	def con10(x):
		return x[3] - 1 - c

	def con11(x):
		return x[4] - 1 - c

	x0 = [1,1,1,1,1]

	constr1 = {'type':'ineq', 'fun':con1}
	constr2 = {'type':'ineq', 'fun':con2}
	constr3 = {'type':'ineq', 'fun':con3}
	constr4 = {'type':'ineq', 'fun':con4}
	constr5 = {'type':'ineq', 'fun':con5}	
	constr6 = {'type':'ineq', 'fun':con6}
	constr7 = {'type':'ineq', 'fun':con7}
	constr8 = {'type':'ineq', 'fun':con8}
	constr9 = {'type':'ineq', 'fun':con9}
	constr10 = {'type':'ineq', 'fun':con10}
	constr11 = {'type':'ineq', 'fun':con11}

	cons = [constr1,constr2,constr3,constr4,constr5,constr6,constr7,constr8,constr9,constr10,constr11]

	solution = minimize(objective,x0,method='SLSQP',constraints=cons)

	x = solution.x[0]
	y = solution.x[1]
	z = solution.x[2]
	a = solution.x[3]
	b = solution.x[4]

	c1 = -x
	c2 = -a*y - 5*b*z
	c3 = -2*a*y
	c4 = -4*a*y
	c5 = -5*a*y - b*z
	
	c6 = -x
	c7 = -a*y - 4*b*z
	c8 = -4*a*y - b*z

	return {'x':x,'y':y,'z':z,'a':a,'b':b},[c1,c2,c3,c4,c5,c6,c7,c8]
######
######

import numpy as np
from scipy.optimize import minimize
from scipy.optimize import fmin_slsqp

def main():
	#x[0] = x
	#x[1] = y
	#x[2] = alpha 

	c = 0.000001

	def objective(x):
		return x[0] * x[1]

	def con1(x):
		return x[0] - x[1] * (x[2]**1) + x[1] * (x[2]**7) - c

	def con2(x):
		return x[0] - x[1] * (x[2]**1) + x[1] * (x[2]**2) - c

	def con3(x):
		return x[0] - x[1] * (x[2]**1) + x[1] * (x[2]**3) - c

	def con4(x):
		return x[0] - x[1] * (x[2]**1) + x[1] * (x[2]**4) - c

	def con5(x):
		return x[1] * (x[2]**7) - x[1] * (x[2]**1) - c

	def con6(x):
		return x[1] * (x[2]**2) - x[1] * (x[2]**1) - c

	def con7(x):
		return x[1] * (x[2]**3) - x[1] * (x[2]**1) - c

	def con8(x):
		return -x[0] + x[1] * (x[2]**4) - x[1] * (x[2]**1) - c

	def con9(x):
		return x[0] + x[1] * (x[2]**1) - x[1] * (x[2]**3) - c

	def con10(x):
		return x[0] + x[1] * (x[2]**7) - x[1] * (x[2]**3) - c

	def con11(x):
		return x[0] + x[1] * (x[2]**2) - x[1] * (x[2]**3) - c

	def con12(x):
		return x[0] + x[1] * (x[2]**4) - x[1] * (x[2]**3) - c

	def con13(x):
		return x[0] - 1 - c 

	def con14(x):
		return x[1] - 1 - c 

	def con15(x):
		return x[2] - c

	x0 = [1,1,1]

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
	constr12 = {'type':'ineq', 'fun':con12}
	constr13 = {'type':'ineq', 'fun':con13}
	constr14 = {'type':'ineq', 'fun':con14}
	constr15 = {'type':'ineq', 'fun':con15}

	cons = [constr1,constr2,constr3,constr4,constr5,constr6,constr7,constr8,constr9,constr10,constr11,constr12,constr13,constr14,constr15]
	solution = minimize(objective,x0,method='SLSQP',constraints=cons)

	#for con in cons:
	#	print(str(con) +': ' + str(con['fun'](solution.x)))

	x = solution.x[0]
	y = solution.x[1]
	a = solution.x[2]

	c1 = -y * (a**1)
	c2 = -x - y * (a**7)
	c3 = -x - y * (a**2)
	c4 = -x - y * (a**3)
	c5 = -x - y * (a**4)

	c6 = -x - y * (a**1)
	c7 = -x - y * (a**7)
	c8 = -x - y * (a**2)
	c9 = -x - y * (a**3)
	c10 = - y * (a**4)

	c11 = -x - y * (a**1)
	c12 = -x - y * (a**7)
	c13 = -x - y * (a**2)
	c14 = - y * (a**3)
	c15 = -x - y * (a**4)

	return {'x':x,'y':y,'a':a},[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15]
######
######

import numpy as np
# from scipy import stats
from scipy.optimize import root 
from scipy.optimize import minimize
from math import cos

# speed = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# x = np.mean(speed)
# print(x)
# y = np.median(speed)
# print(y)
# z = stats.mode(speed)
# print(z)
# k = np.std(speed)
# print(k)
# v = np.var(speed)
# print(v)
# print(dir(stats))

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
p = np.percentile(ages,90)
print(p)

# def eqn(x):
#     return x + cos(x)

# myroot = root(eqn,0)
# print(myroot)

# def eqn(x):
#     return x**2+x+2

# mymin = minimize(eqn,0,method="BFGS")
# print(mymin)
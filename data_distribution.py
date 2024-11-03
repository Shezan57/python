import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order

# dataSet = np.random.normal(5.0,1.0,100000)
# plt.hist(dataSet,100)
# plt.show()

# age = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# slope, intercept, r, p, std_err = stats.linregress(age,speed)

# def myfunc(x):
#     return slope*x + intercept

# mymodel = list(map(myfunc,age))

# print(r)
# speed1 = myfunc(10)
# print(speed1)
# plt.scatter(age,speed)
# plt.plot(age,mymodel)
# plt.show()

# arr = np.array([
#     [0,1,2],
#     [1,0,0],
#     [2,0,0]
# ])

# newarr = csr_matrix(arr)
# print(connected_components(newarr))
# print(dijkstra(newarr,return_predecessors=True,indices=0))
# print(floyd_warshall(newarr,return_predecessors=True))
# print(bellman_ford(newarr,return_predecessors=True,indices=0))

arr = np.array([
    [0,1,0,1],
    [1,1,1,1],
    [2,1,1,0],
    [0,1,0,1]
])

newarr = csr_matrix(arr)

print(depth_first_order(arr,1))
print(breadth_first_order(arr,1))
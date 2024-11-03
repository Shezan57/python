import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
# 1D array

# oneDarr = np.array([1,2,3,4,5,6])
# print(oneDarr)
# print(oneDarr[1:5])
# print(oneDarr[1:5:2])
# print(oneDarr[0:6:2])
# for idx, x in np.ndenumerate(oneDarr):
#     print(idx,x)

# 2D array
# twoDarray = np.array([[1,2,3,10,11,12],[4,5,6,7,8,9]])
# print(twoDarray)
# print(twoDarray[0,1])
# print(twoDarray[1,2])
# print(twoDarray[1,1:4])
# print(twoDarray[0:2,2])
# print(twoDarray.shape)
# for x in np.nditer(twoDarray[:, ::2]):
#     print(x)
# for idx, x in np.ndenumerate(twoDarray):
#     print(idx, x)


# 3D array
# threeDarray = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])
# print(threeDarray)
# print(threeDarray[0,1,2])
# print(threeDarray[1,0,1])

# print dimension
# print(oneDarr.ndim)
# print(twoDarray.ndim)
# print(threeDarray.ndim)
# for x in np.nditer(threeDarray):
#     print(x)

# create user define dimension array
# nDimenstionArray = np.array([1,2,3,4,5], ndmin= 5)
# print(nDimenstionArray)
# print("The arrays dimenstion is: ",nDimenstionArray.ndim)
# print("shape of the array: ", nDimenstionArray.shape)


# arr = np.array([1,3,4,5,6,7])
# x = arr.view()
# x[0] = 31
# print(arr)
# print(x)


# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr = np.stack((arr1,arr2),axis=1)
# arr = np.concatenate((arr1,arr2),axis=0)
# arr = np.hstack((arr1,arr2))
# arr = np.vstack((arr1,arr2))
# arr = np.dstack((arr1,arr2))
# print(arr)
# newarr = np.array_split(oneDarr,4)
# print(newarr)

# x = np.where(oneDarr == 4)
# print(x)
# x = np.searchsorted(oneDarr,4)
# print(x)

# arr = np.array([41,42,43,44])
# filter_array = []
# for element in arr:
#     if element > 42:
#         filter_array.append(True)
#     else:
#         filter_array.append(False)

# newArray = arr[filter_array]
# print(filter_array)
# print(newArray)
# filter_array = arr > 42
# new_array = arr[filter_array]
# print(filter_array)
# print(new_array)

# ----------------------Random-------------------------

# x = random.choice([3,5,7,9], p=[0.3,0.4,0.1,0.2], size=(100))
# print(x)

# x = random.choice([3,4,7,9], p=[0.1,0.3,0.6,0.0], size=(3,5))
# print(x)

# arr = np.array([1,2,3,4,5])
# # random.shuffle(arr)
# # print(arr)
# print(random.permutation(arr))
# sns.displot([0,1,2,3,4,5], hist=False)
# plt.show()

# x = random.normal(size=(2,3))
# print(x)

# x = random.normal(loc=1,scale=2,size=(2,3))
# print(x)

# sns.displot(random.normal(size=1000),)
# plt.show()

# x = random.binomial(n=10, p=0.5, size=10)
# print(x)

# sns.displot(random.binomial(n=10,p=0.5,size=1000), kde = True)

# sns.displot(random.normal(loc=50,scale=5,size=1000),label = 'normal')
# sns.displot(random.binomial(n=100,p=0.5,size=1000),label = 'binomial')
# plt.show()


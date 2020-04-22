# import numpy as np
#
# arr = np.array([1,2,3,4,5])
# x = arr.copy()
# #NumPy array copy
# arr[2] = 58
# #print(x)
# print(arr)


# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# #NumPy array view
# x[3] = 100
#
# print(arr)
# print(x)

# import numpy as np
# #checking if array owns it's data
# arr = np.array([1, 2, 3, 4, 5])
# y = arr.copy()
# x = arr.view()
# print(x.base)
# print(y.base)

# import numpy as np
# #shape of an array
# arr = np.array([[[1,2,3,4, 45.87], [5,6,7,8,9]]])
# print(arr.shape)

# import numpy as np
# arr = np.array([1,2,3,4], ndmin=5)
# print(arr)
# print('shape of the array:', arr.shape)

# import numpy as np
# #flattening the multiD. array to 1D array
# arr = np.array([[1,2,3,4], [5,6,7,8], [9,5,8,7]])
# newarr = arr.reshape(-1)
# print(newarr)

# import numpy as np
# #terating on each scalar element of the 2-D array
# arr = np.array([[1,2,3],[4,5,6]])
# for i in arr:
#     for j in i:
#         print(j)

# import numpy as np
# #Iterating 3-D Arrays
# arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
# for x in arr:
#     print(x)
#
# import numpy as np
#
# # Iterating 3-D Arrays(scalar)
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#     for y in x:
#         print(y)

# import numpy as np
# #Iterating on each scalar element
# arr = np.array([[[1, 2], [3, 4], [0.56,999]], [[5, 6], [7, 8], [8,10.56]]])
#
# for x in np.nditer(arr):
#   print(x)

# import numpy as np
#
# arr = np.array([1,2,3,4,5])
#
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)
#   print(arr.dtype)

# import numpy as np
#
# arr = np.array([[1,2,3,4], [5,6,7,8]])
#
# for i in np.nditer(arr[:, ::3]):
#     print(i)

# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# for i, j in np.ndenumerate(arr):
#     print(i,j)

# import numpy as np
# arr = np.array([[1,2,3], [4,5,6]])
# for i, j in np.ndenumerate(arr):
#     print(i,j)

#Joining two arrays
# import numpy as np
#
# arr1 = np.array([[1, 2, 3], [4,5,6]])
# arr2 = np.array([[7,8,9], [10,11,12]])
# arr3 = np.array([[13,14,15], [16,17,18]])
#
# arr = np.concatenate((arr1, arr2, arr3), axis=1)
# print(arr)

# import numpy as np
# #stacking along rows
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
#
# arr = np.hstack((arr1, arr2))
# print(arr)
#
#
# import numpy as np
# #stacking along columns
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
#
# arr = np.vstack((arr1, arr2))
# print(arr)
#
# import numpy as np
# #stacking along columns
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
#
# arr = np.dstack((arr1, arr2))
# print(arr)

# # splitting and accessing arrays
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 4)              # split() can also be used, but array_split() works in all conditions:)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])
# print(newarr[3])

# # splitting 3D array with axis
# import numpy as np
#
# arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
#
# newarr = np.dsplit(arr, 3)
#
# print(newarr)

# import numpy as np
# a = np.arange(16).reshape (4,2,2)
# print(a)

# import numpy as np
# # searching array(s)
# arr = np.array([1, 2, 3, 4, 5, 6, 5.0, 5])
# srh = np.where(arr == 5)
# print(srh)

# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# x = np.where(arr % 2 == 0)
# print(x)

# import numpy as np
# arr = np.array([10, 20, 30, 40, 50, 60])
# ss = np.searchsorted(arr, [20,40, 60])    # for multiple arrays
# print(ss)

# import numpy as np
# arr = np.array(['v', 'G', 'u', 'a', 'C'])
# print(np.sort(arr))

# import numpy as np
# arr = np.array(['Madhu', 'programmer', 'mad', 'pYthoN'])
# print(np.sort(arr))

# import numpy as np
# arr = np.array([True, False, True, False])  #since the int value for false is "0"
# print(np.sort(arr))

# import numpy as np
# # array filtering
# arr = np.array([100, 200, 300, 400, 500])
# x = [True, False, True, False, True]
# newarr = arr[x]
# print(newarr)

# import numpy as np
#
# arr = np.array([50, 60, 70, 80])
# filt_arr = []
# for ele in arr:
#     if ele > 60:
#         filt_arr.append(True)
#     else:
#         filt_arr.append(False)
#
# newarr = arr[filt_arr]
#
# print(filt_arr)
# print(newarr)


# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# filt = []
# for x in arr:
#     if x % 2 == 0:
#         filt.append(True)
#     else:
#         filt.append(False)
#
# new_arr = arr[filt]
#
# print(filt)
# print(new_arr)

# import numpy as np
# arr = np.array([41, 42, 43, 44])
# filt_arr = arr > 42
# newarr = arr[filt_arr]
#
# print(filt_arr)
# print(newarr)

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# filter_arr = arr % 2 == 0
#
# newarr = arr[filter_arr]
#
# print(filter_arr)
# print(newarr)


##### NumPy random numbers #####

# from numpy import random
# x = random.randint(10)   #int
# print(x)
#
#
# from numpy import random
# x = random.rand()   #random floaat b/w 0-1
# print(x)


# from numpy import random
# x = random.randint(10,20, size=(5))    # printing 5 random integers from 10-20
# print(x)

# from numpy import random
# x = random.randint(10, 40, size=(2, 5))
# print(x)

# from numpy import random
# x = random.rand(3)
# print(x)

# from numpy import random
# x = random.rand(3, 5)
# print(x)

# from numpy import random
# x = random.choice([1, 2, 3, 4, 5, 6])
# print(x)

# from numpy import random
# a = random.randint([2, 4, 6, 8, 10], size = (3,5))
# print(a)

# ### Data distribution ###
# from numpy import random
# x = random.choice([2, 4, 6, 8], size=(3, 5), p=[0.05, 0.1, 0.2, 0.65])
# print(x)

# ### Random permutation ###
# from numpy import random
# import numpy as np
#
# x = np.array([1, 2, 3, 4, 5])
# print(random.shuffle(x))
# print(x)

# from numpy import random
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5])
#
# print(random.permutation(arr))
# print(x)

# from numpy import random
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(random.permutation(arr))


# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.distplot([0, 10, -20, 3, 40.848, 50])
# plt.show()
#

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.distplot(random.normal(size = 10), hist = False)
# plt.show()

# ### Visualization of Binomial distribution (discrete) ###
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.distplot(random.binomial(n = 20, p = 0.7, size = 1000), hist = True, kde = False)
# plt.show()

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.distplot(random.normal(loc=100, scale=25, size=1000), hist=False, label='normal')
# sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
#
# plt.show()

# def calculateSquare(n):
#   return n*n
#
# numbers = (1, 2, 3, 4)
# result = map(calculateSquare, numbers)
# print(result)
#
# # converting map object to set
# numbersSquare = set(result)
# print(numbersSquare)

### uniform distribution ###
#
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.distplot(random.uniform(size=1000), hist = False)
# plt.show()

### Logistic Distribution ###
#
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.distplot(random.logistic(loc=3, scale=5, size=(2, 3)), hist = False)
# plt.show()

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
# sns.distplot(random.logistic(size=1000), hist=False, label='logistic')      ## Difference between normal and logistics ##
#
# plt.show()

# from numpy import random
# x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])   # multinomial distribution #
# print(x)

# Exponential Distribution #

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(scale = 2, size=1000), hist=False)

plt.show()
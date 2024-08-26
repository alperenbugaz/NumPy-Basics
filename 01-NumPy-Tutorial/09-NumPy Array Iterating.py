import numpy as np

#Iterating Arrays
arr = np.array([1, 2, 3])

for x in arr:
  print(x) # 1 2 3

#Iterating 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x) # [1 2 3] [4 5 6]

for x in arr:
  for y in x:
    print(y) # 1 2 3 4 5 6

#Iterating 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x) # [[1 2 3] [4 5 6]] [[ 7  8  9] [10 11 12]]

for x in arr:
  for y in x:
    for z in y:
      print(z) # 1 2 3 4 5 6 7 8 9 10 11 12

#Iterating Arrays Using nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x) # 1 2 3 4 5 6 7 8

#Iterating Array With Different Data Types
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x) # b'1' b'2' b'3'

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x) # 1 3 5 7

#Enumerated Iteration Using ndenumerate()
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x) # (0,) 1 (1,) 2 (2,) 3

import numpy as np

#Sorting Arrays
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]

print(newarr) # [41 43]

#Creating the Filter Array
arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr) # [False, False, True, True]
print(newarr) # [43 44]



arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr) # [False, True, False, True, False, True, False]
print(newarr) # [2 4 6]

#Creating Filter Directly From Array
arr = np.array([41, 42, 43, 44])

filter_arr = []

for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr) # [False, False, True, True]
print(newarr) # [43 44]

#Creating Filter Directly From Array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_array = arr > 3
newarr = arr[filter_array]
print(filter_array) # [False, False, False, True, True, True, True]
print(newarr) # [4 5 6 7]

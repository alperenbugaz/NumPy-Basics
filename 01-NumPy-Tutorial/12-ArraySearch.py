import numpy as np

#Searching Arrays
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)

print(x) # (array([3, 5, 6]),)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)

print(x) # (array([1, 3, 5, 7]),)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)

print(x) # (array([0, 2, 4, 6]),)

#Search Sorted
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
y = np.searchsorted(arr, 9)
print(x) # 1
print(y) # 3

#Search From the Right Side
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
y = np.searchsorted(arr, 8, side='right')
z = np.searchsorted(arr, 8, side='left')

print(x) # 2
print(y) # 3
print(z) # 2

#Multiple Values
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6]) # sıralı bir dizi içinde hangi indekse yerleştirileceğini bulur.

print(x) # [1 2 3]

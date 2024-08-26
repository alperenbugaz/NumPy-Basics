import numpy as np

#Splitting NumPy Arrays

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)

print(newarr) # [array([1, 2]), array([3, 4]), array([5, 6])]

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)

print(newarr) # [array([1, 2]), array([3, 4]), array([5]), array([6])]

#Split Into Arrays
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0]) # [1 2]
print(newarr[1]) # [3 4]
print(newarr[2]) # [5 6]

#Splitting 2-D Arrays
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr) # [array([[1, 2], [3, 4]]), array([[5, 6], [7, 8]]), array([[ 9, 10], [11, 12]])]
    #Split the 2-D array into three 2-D arrays.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)

print(newarr) #[array([[1, 2, 3],[4, 5, 6]]), array([[ 7,  8,  9],[10, 11, 12]]), array([[13, 14, 15],[16, 17, 18]])]

    #Split the 2-D array into three 2-D arrays along rows.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)

print(newarr) # [array([[ 1],[ 4],[ 7],[10],[13],[16]]), array([[ 2],[ 5],[ 8],[11],[14],[17]]), array([[ 3],[ 6],[ 9],[12],[15],[18]])]

#hsplit(), hstack() yerine alternatif olarak kullanılabilir.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)


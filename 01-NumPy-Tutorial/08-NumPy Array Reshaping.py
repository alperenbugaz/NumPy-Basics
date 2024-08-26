import numpy as np

#Reshape From 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print("1-D'den 2-D'ye reshape:",newarr) # [[ 1  2  3] [ 4  5  6] [ 7  8  9] [10 11 12]]

#Reshape From 1-D to 3-D
newarr = arr.reshape(2, 3, 2)
print("1-D'den 3-D'ye reshape:",newarr) # [[[ 1  2] [ 3  4] [ 5  6]] [[ 7  8] [ 9 10] [11 12]]]

#Can We Reshape Into any Shape?
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#
# newarr = arr.reshape(3, 3)
#
# print(newarr) # ValueError: cannot reshape array of size 8 into shape (3,3)

#Returns Copy or View?
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base) #
#.base: base özelliği, bu yeniden şekillendirilmiş dizinin (view) orijinal diziyle olan ilişkisini gösterir.
#Eğer bir NumPy dizisi başka bir dizinin görünümü (view) ise, .base özelliği, bu yeni dizinin hangi diziden türediğini (orijinal diziyi) gösterir.

#Unknown Dimension
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr) # [[[1 2] [3 4]] [[5 6] [7 8]]]

#Flattening the arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr) # [1 2 3 4 5 6]
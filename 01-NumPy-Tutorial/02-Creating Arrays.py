import numpy as np

#Bir ndarray oluşturmak için, bir listeyi, tuple'ı veya herhangi bir dizi benzeri nesneyi array() yöntemine aktarabiliriz.Bu, bir ndarray'e dönüştürülecektir.
ndarray_arr = np.array([1, 2, 3, 4, 5]) #ndarray nesnesi oluşturduk.

print ("Numpy Dizisi:",ndarray_arr)
print("Numpy dizisinin tipi:",type(ndarray_arr)) #dizinin tipini ekrana yazdırdık.

numpy_arr = np.array((1, 2, 3, 4, 5))
print ("Numpy Dizisi:",numpy_arr)
print("Numpy dizisinin tipi:",type(numpy_arr))

#0D array: 0D array, bir değer içerir. Bu, bir dizi oluşturduğumuzda, 0D array oluşturduğumuz anlamına gelir.
zeroD_arr = np.array(42) #0D array oluşturduk.
print("0D Numpy Dizisi:",zeroD_arr)

#1D array: 1D array, bir dizi oluşturduğumuzda, 1D array oluşturduğumuz anlamına gelir.
oneD_arr = np.array([1, 2, 3, 4, 5]) #1D array oluşturduk.
print("1D Numpy Dizisi:",oneD_arr)

#2D array: 2D array, bir dizi oluşturduğumuzda, 2D array oluşturduğumuz anlamına gelir.
twoD_arr = np.array([[1, 2, 3], [4, 5, 6]]) #2D array oluşturduk.
print("2D Numpy Dizisi:",twoD_arr)

#3D array: 3D array, bir dizi oluşturduğumuzda, 3D array oluşturduğumuz anlamına gelir.
threeD_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #3D array oluşturduk.
print("3D Numpy Dizisi:",threeD_arr)

#Check Number of Dimensions
#NumPy dizilerinin sayısını kontrol etmek için ndim özelliğini kullanabiliriz.
print("0D Numpy Dizisinin Boyutu:",zeroD_arr.ndim)
print("1D Numpy Dizisinin Boyutu:",oneD_arr.ndim)
print("2D Numpy Dizisinin Boyutu:",twoD_arr.ndim)
print("3D Numpy Dizisinin Boyutu:",threeD_arr.ndim)


#Higher Dimensional Arrays
arrhda = np.array([1, 2, 3, 4], ndmin=7)

print("arrhda dizisi:",arrhda)
print('number of dimensions :', arrhda.ndim)



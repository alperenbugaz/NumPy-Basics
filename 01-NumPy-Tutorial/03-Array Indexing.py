import numpy as np


arr = np.array([1, 2, 3, 4])
print("Dizinin ilk indisi",arr[0]) #dizinin ilk elemanını ekrana yazdırdık.
print("Dizinin ikinci indisi",arr[1]) #dizinin ikinci elemanını ekrana yazdırdık.
print("Dizinin ilk ve sonuncu indisinin toplamı:",arr[0]+arr[3]) #dizinin üçüncü elemanını ekrana yazdırdık."

#Access 2-D Arrays
arr2d = np.array([[1,2,3,4,5], [6,7,8,9,10]]) #2D array oluşturduk.
print("2D Array:",arr2d) #2D array'i ekrana yazdırdık.
print("2D Array'in 1. satırı:",arr2d[0]) #2D array'in 1. satırını ekrana yazdırdık.
print("2D Array'in 2. satırı:",arr2d[1]) #2D array'in 2. satırını ekrana yazdırdık.
print("2D Array'in 1. satırının 1. elemanı:",arr2d[0, 1]) #2D array'in 1. satırının 1. elemanını ekrana yazdırdık.
print("2D Array'in 2. satırının 2. elemanı:",arr2d[1, 1]) #2D array'in 2. satırının 2. elemanını ekrana yazdırdık.

#Access 3-D Arrays
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) #3D array oluşturduk.
print("3D Array:",arr3d) #3D array'i ekrana yazdırdık.
print("3D Array'in 1. satırı:",arr3d[0]) #3D array'in 1. satırını ekrana yazdırdık.
print("3D Array'in 2. satırı:",arr3d[1]) #3D array'in 2. satırını ekrana yazdırdık.
print("3D Array'in 1. satırının 1. elemanının ilk indisi:",arr3d[0, 0, 0])
print("3D Array'in 2. satırının 2. elemanının ikinci indisi:",arr3d[1, 1, 1])

#Negative Indexing
print("Dizinin son elemanı:",arr[-1]) #dizinin son elemanını ekrana yazdırdık.
print("2D Array'in 1. satırının son elemanı:",arr2d[0, -1]) #2D array'in 1. satırının son elemanını ekrana yazdırdık.
print("3D Array'in 1. satırının 1. elemanının son indisi:",arr3d[0, 0, -1]) #3D array'in 1. satırının 1. elemanının son indisi ekrana yazdırdık.
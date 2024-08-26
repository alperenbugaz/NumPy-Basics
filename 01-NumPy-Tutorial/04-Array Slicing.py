import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) #1. indisten 5. indise kadar olan elemanları ekrana yazdırdık.
print(arr[4:]) #4. indisten sona kadar olan elemanları ekrana yazdırdık.
print(arr[:4]) #Baştan 4. indise kadar olan elemanları ekrana yazdırdık.

#Negative Slicing
print(arr[-3:-1]) #Dizinin sondan 3. elemanından sondan 1. elemana kadar olan elemanları ekrana yazdırdık.

#STEP
print(arr[1:5:2]) #1. indisten 5. indise kadar olan elemanları 2'şer 2'şer atlayarak ekrana yazdırdık.
print(arr[::2]) #Baştan sona kadar olan elemanları 2'şer 2'şer atlayarak ekrana yazdırdık.

#Slicing 2-D Arrays
arr2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]) #2D array oluşturduk.
print(arr2d[1, 1:4]) #2D array'in 1. satırının 1. indisten 4. indise kadar olan elemanları ekrana yazdırdık.
import numpy as np


arr_int = np.array([1, 2, 3, 4])
print("arr_int dizisinin data tipi:",arr_int.dtype)

arr_str = np.array(['apple', 'banana', 'cherry'])
print("arr_str dizisinin data tipi:",arr_str.dtype)



arr_i4 = np.array([1, 2, 3, 4], dtype='i4') #i4: 4 byte integer

print("arr_i4 data tipi",arr_i4.dtype)

#What if a Value Can Not Be Converted?
#'a' gibi tam sayı olmayan bir dize, tam sayıya dönüştürülemez (bir hataya neden olur):
#arr_i4 = np.array(['a', '2', '3', '4'], dtype='i') #i: integer
#print("arr_i4 data tipi",arr_i4.dtype)

#Traceback (most recent call last):
#  File "05-Data Types.py", line 17, in <module>
#    arr_i4 = np.array(['a', '2', '3', '4'], dtype='i') #i: integer
#             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#ValueError: invalid literal for int() with base 10: 'a'

#Converting Data Type on Existing Arrays
arr_convert1 = np.array([1.1, 2.1, 3.1])
newarr1 = arr_convert1.astype('i') #i: integer
print("arr_convert1 dizisinin data tipi:",arr_convert1.dtype) #int değeri float değerine dönüştürüldü.
print("newarr1 dizisinin data tipi:",newarr1.dtype) #

arr_bool = np.array([1, 0, 3])

newarr_bool = arr_bool.astype(bool)

print("Newarr_bool dizisi:",newarr_bool)
print("Newarr dizisi data tipi: ",newarr_bool.dtype)
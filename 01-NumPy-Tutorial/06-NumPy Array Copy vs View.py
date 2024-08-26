import numpy as np

#Copy
#Kopyada yapılan değişiklikler orijinal diziyi etkilemez ve orijinal dizide yapılan değişiklikler kopyayı etkilemez.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#View
#View'da yapılan değişiklikler orijinal diziyi etkiler ve orijinal dizide yapılan değişiklikler view'ı etkiler.
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)
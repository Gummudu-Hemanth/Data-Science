# -> Selects the indices or elements from the array.
arr = np.array([[1,2,3,4,5] , [6,7,8,9,10] , [11,23,44,56,78]])
b = np.nonzero(arr>5)
print(b)
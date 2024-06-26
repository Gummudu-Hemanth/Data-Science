import numpy as np

'ARRAYS'

# One Dimensional Arrray
list = [1,2,3,4,5] # Created a list

# Creating a numpy array
arr = np.array(list)

print("The list in python: " , list) # Output =  [1, 2, 3, 4, 5]
print("The arrays in python: " , arr) # Output = [1 2 3 4 5]

# Checking the datatypes
print(type(list))
print(type(arr))

# Accessing the elements using integer index.
print(arr[0]) # 1
print(arr [:2]) # [1 2]

# Slicing an arrays return us view. View is an object that refer to the original array

list = [1,2,3,4,5,6,7,8,9] # Created a list
arr = np.array(list) # Creating a array
print(arr)

b = arr [4:]
print(b) # [5 6 7 8 9]

b[2] = 70 # Changing the value.

print(arr) # [ 1  2  3  4  5  6 70  8  9]

# In arrays elemets can be accessed by specifying index along with the axis within a single square brackets.

arr = np.array([[1,2,3,4] , 
				[5,6,7,8] , 
				[9,10,11,12]]) # created an array
# print(arr)
# print(type(arr))

print(arr[2 , 2]) # 11
print(arr[1 , 3]) # 8

'ARRAYS ATTRIBUTES'

# 1. ndim
arr = np.array([[1,2,3,4,5],
				[6,7,8,9,10],
				[2,4,6,8,10]])

print(arr.ndim) # 2

# 2. shape
arr = np.array([[1,2,3,4,5],
				[6,7,8,9,10],
				[2,4,6,8,10]])

print(arr.shape) # (3,5) because 3 rows and 5 columns.

# 3 dtype
arr = np.array([[1,2,3,4,5],
				[6,7,8,9,10],
				[2,4,6,8,10]])

print(arr.dtype) # int

# 4. size
arr = np.array([[1,2,3,4,5],
				[6,7,8,9,10],
				[2,4,6,8,10]])

print(arr.size) # 15 total number of elements in 2d array.

'Creating Basic Arrays'

# 1. np.zeros()
arr = np.zeros(4 , dtype=int)
print(arr)

# 2. np.ones()
arr = np.ones(4 , dtype=int)
print(arr)

# 3. np.arange()
arr = np.arange(5)
print(arr)

# 4. np.empty()
arr = np.empty(4 , dtype=int)
print(arr)

# 5. np.linspace()
arr = np.linspace(0,10,num=3,dtype=int)
print(arr)

'INDEXING AND SLICING'

arr = np.array([[1,2,3,4,5] , [6,7,8,9,10] , [11,23,44,56,78]])

print(arr[0][3]) # 4
print(arr[2]) #  [11,23,44,56,78]

# Printing all the values of array less than 9.
arr = np.array([[1,2,3,4,5] , [6,7,8,9,10] , [11,23,44,56,78]])
fil = (arr[arr<9]) # [1 2 3 4 5 6 7 8]
print(fil)

print(arr[arr <=5]) # [1 2 3 4 5]

# Non-zero
# -> Selects the indices or elements from the array.
arr = np.array([[1,2,3,4,5] , [6,7,8,9,10] , [11,23,44,56,78]])
b = np.nonzero(arr>5)
print(b)

'OPERATIONS ON NUMPY ARRAYS'
arr1 = np.arange(4 , dtype=int).reshape(2,2)
print("First array: " ,"\n" , arr1 , "\n")

arr2 = np.array([12,10])
print("Second Array: " , "\n" , arr2 , "\n")

# Adding Two Arrays
print("Adding two arrays: " , "\n" , np.add(arr1 , arr2) , "\n")

# Subtracting Two Arrays
print("Subtracting two arrays: " , "\n" , np.subtract(arr1 , arr2) , "\n")

# Multiplication of two arrays
print("Multiplying two arrays: " , "\n" , np.multiply(arr1 , arr2) , "\n")

# Dividing tw arrays
print("Dividing two arrays: " , "\n" , np.divide(arr1 , arr2))

# Recoprocal Function
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.reciprocal(arr))

# Power method
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.power(arr , 3))

'BROADCASTING'
arr = np.array([[1,2,3,4,5] , [6,7,8,9,0]])
print(arr * 2)

'Statistical Operation'
# 1. Sum -> Return the sum of the array.
arr = np.array([1,2,3,4,5])
print(arr.sum()) # 15

# 2. Min -> Returns the minimum value in the array
arr = np.array([1,2,3,4,5])
print(arr.min()) # 1

# 3. Max -> Return the maximun value in the array
arr = np.array([1,2,3,4,5])
print(arr.max()) # 5

# 4. mean -> sum of elements / total number of elements.
arr = np.array([1,2,3,4,5])
print(arr.mean()) # 3.0

# 5. STd
arr = np.array([1,2,3,4,5])
# print(arr.std()) # 1.4142135623730951

'Transpose and Reshape'

# Transpose -> In the given matrix Rows becomes the columns and columns become the rows
arr = np.array([[1,2,3] , [4,5,6]])
print("Array before transpose: " , "\n" , arr , "\n")
print("Array after transpose: " , "\n" , arr.transpose())

# Reshape ->  Changing the shape of an array
# -> 1D array to 2D or 3D array.

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12]) # This is my 1D array
print("This is 1D array: " , "\n" , arr , "\n")
print("Converted to 2D array: " , "\n" , arr.reshape(2,6) , "\n")
print("Converted to 3D arrays: " , "\n" , arr.reshape(2,3,2))

'Stacking and Spliting of Numpy Arrays'

# Stacking
arr = np.array([1,2,3])
arr1= np.array([4,5,6])
res = np.vstack((arr,arr1))
res1 = np.hstack((arr,arr1))

print("This is the Vertical stacking array: " , "\n" , res , "\n")
print("This is the Horizontal stacking array: " , "\n" , res1 , "\n")

# Splitting
arr = np.arange(9)
split = np.split(arr,3) # splitting the arrays into three equal parts.
print(split)

'VIEWS AND COPIES OF ARRAYS'

# Views
arr = np.array([1,2,3,4,5])
view = arr.view()

arr[0] = 100
print("Original array:- " , arr , "\n")
print("View array:- " , view)

# Copy
arr = np.array([1,2,3,4,5,6])
copy = arr.copy()

arr[0] = 100
print("Original Array:- " , arr)
print("Copy Array:- " , copy)

'CHECKING IF ARRAYS IS A VIEW OR A COPY'
arr = np.array([1,2,3,4,5,6])

view = arr.view()
copy = arr.copy()

print(view.base) # It will return the original array
print(copy.base) # It will return NONE
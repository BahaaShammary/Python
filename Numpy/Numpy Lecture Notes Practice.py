#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
# Creating an array in Numpy
a = np.array([2, 3, 4])
print(a)


# In[2]:


# Another way of creating an array: Using arange to create an array
b = np.arange(1, 12, 2)
print(b)


# In[5]:


# Another way of creating an array: Using linspace (creates floating points)
c = np.linspace(1, 12, 6) # 6 means we need six elements from 1 to 12 that are evenly spaced
print(c) # Generates a list of floats by default


# In[6]:


# We can reshape an array into two dimensional array
d = c.reshape(3, 2) # reshape into 3 rows and two columns
print(d)


# In[7]:


# Lecture Code: Creating and appending new item or items to an array
arr = np.array([5.2, 4.3, 3.1], float)
print(arr)
arr2 = np.append(arr, [3.3, 3.4, 3.5])
print(arr2)
arr3 = np.array([1.2, 1.4])
print(arr3)


# In[8]:


# Concatenate two arrays 
arr4 = np.concatenate((arr, arr3))
print(arr4)


# In[9]:


# Adding value at a specific index
arr5 = np.array([1, 3, 4, 5])
print(arr5)
arr5 = np.insert(arr5, 1, 2) # Add the arry you want to add to, the index, the value to be added
print(arr5)


# In[10]:


# Delete a value at a specific index
arr6 = np.delete(arr5, 4) # The array and the index to be deleted
print(arr6)


# In[11]:


# Access a value using squared brackets
print(arr6[2])


# In[12]:


# Multi dimensional array
darr = np.array([[1 , 2, 3], [4, 5, 6]])
print(darr)
print(darr[1, 2])


# In[14]:


darr[0, 1] = 12
print(darr[0])


# In[15]:


# Slicing arrays
arr7 = darr[:,0] # This extracts all rows of a single column
print(arr7)


# In[16]:


# Changing all values in a single column
darr[:,0] = 20
print(darr)


# In[17]:


# Changing all values in a single row
darr[0,:] = 21
print(darr)


# In[18]:


# Retrieve certain rows and columns
darr1 = np.array([[14.4, 2.4, 3.5], [54.3, 34.4,
98.22], [100, 200, 300]], float)
print (darr1)
print (darr1[0:2, 0:2]) # print row 0 and 1 not including 2 and print column 0 and 1 not including 2


# In[19]:


# Select a number of columns from a matrix to make flat array
darr2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [10, 11, 12, 13]])
print (darr2)

darr3 = darr2[:, 1:3] # Getting all rows but only column 1 and 2 not including 3
print (darr3)

darr3 = darr2[:, 3] # Getting all rows and column 3
print (darr3)


# In[20]:


# Access specific rows - row 1, 2 and 3 - row 0 and 1
darr4 = darr2[1:4, 0:2]
print(darr4)


# In[21]:


darr4 = np.array([[14.4, 2.4, 56.4], [54.3, 34.4, 98.22]])
print(darr4)
# Getting length of 2D array
print(len(darr4))

# Getting length of 2D array row
print(len(darr4[0]))


# In[22]:


# Slicing
data = np.array([[1, 2, 3], [2, 4, 5], [4, 5, 7],
[6, 2, 3]])
print('The original 2d array \n{}'.format(data))

resultA = data[:, 0] # getting a new list from slicing the 2d array and saving it in a variable
print('Getting a slice from the original 2d array\n{}'.format(resultA))

resultA[0] = 200 # Changing one of the elements in the new array 
print ('A value from the slice has been changed\n{}'.format(resultA))
print ('The original 2d array has also been changed\n{}'.format(data)) # The original 2d array is changed even though we changed the resultA variable
# That's because the new array is pointing to the same data in memory as the original array


# In[3]:


# If we don't want to change the original 2d array, then use numpy.copy function or np.copy(array)
# So redo the same code as the above but use np.copy(data) and see how when we change a value in the new array, it doesn't affect the original
data1 = np.array([[1, 2, 3], [2, 4, 5], [4, 5, 7],
[6, 2, 3]])
print('The original 2d array \n{}'.format(data1))
data1Copy = np.copy(data1) # Copying the 2d array to another variable
print('The copied 2d array \n{}'.format(data1Copy)) # getting same as original 2d array

data1Copy[0,0] = 200 # Changing one of the elements in the new array does not affect the original 2d array 
print('The copied 2d array is changed: \n{}'.format(data1Copy)) 
print ('The original 2d array remains unchanged \n{}'.format(data1)) # The original 2d array is not changed because the copy array is not pointing to the same values in memory as the original.


# In[23]:


# Reading data from a file in numpy - It generates a matrix from the numbers in the file
data = np.genfromtxt('numbers.txt', dtype=int)
print(data)
print (data[0,0])
print (data[1,0])
print (data[2,0])
print (data[3,0])


# In[24]:


# Save data to file using numpy
sliced_data = data[:3,0:3]
print(sliced_data)
#np.savetxt('numbersWithNumpy.txt', sliced_data)


# In[28]:


# Auto populate a two dimensional array with zeros
zeros = np.zeros((3,3))
print(zeros)


# In[25]:


# Using 'in' in 2d arrays
arr10 = np.array([[14.4, 2.4, 56.4], [54.3, 34.4, 98.22]], float)
if 2.4 in arr10:
    print ("Found")
else:
    print ("Not Found")


# In[32]:


import numpy as np
data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter = ',')
count = data[:, 12]
print(count)
total = 0.0
for value in count:
    total += value
print(total)
print ("Average wind is ", total/len(count))


# In[33]:


# Appending to a two dimensional array
arr11 = np.array([[14.4, 2.4, 56.4], [54.3, 34.4, 98.22]], float)
print(arr11)


# In[41]:


arr12 = np.append(arr11, [[1.5,1.6,1.7]], axis = 0) # Added 3 values at the last row (axis 0)
print(arr12)


# In[51]:


arr13 = np.append(arr12, [[1.8],[1.9], [2.1]], 1) # Added 3 values at the last column (axis 1)
print(arr13)


# In[58]:


# Getting Min and Max of a 2D array
arr14 = np.array([10,20,30], float)
arr15 = np.array([1,2,3], float)
max = np.amax(arr14)
print(max)
min = np.amin(arr15)
print(min)


# In[60]:


arr16 = np.amax(arr13, 0) # Getting a list of max values from the rows 
print(arr16)
arr16 = np.amin(arr13, 1) # Getting a list of max values from the columns 
print(arr16)


# In[69]:


# Performing operations on arrays - can also be done to 2D arrays
arr17 = np.array([[1, 2, 4],[3, 4, 2]], float)
print(arr17)
print('Sum of the whole 2D array: {}'.format(np.sum(arr17)))
print('Product of whole 2D array: {}'.format(np.product(arr17)))
print('Sum of each column from 2D array: {}'.format(np.sum(arr17, axis = 0)))
print('Sum of each row from 2D array: {}'.format(np.sum(arr17, axis = 1)))
print('Mean of rows from 2D array: {}'.format(np.mean(arr17, 1)))


# In[ ]:


# Perform more statistical operations: 
arr18 = np.array([2, 1, 9], float)
print (np.mean(arr18))
print (np.var(arr18))
print (np.std(arr18))


# In[72]:


# Getting the average wind speed from file
data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter = ',')
print (np.mean(data[:, 12]))


# In[74]:


# Getting the mean, the max and min of casual users
print(np.mean(data[:, 13]))
print(np.amax(data[:, 13]))
print(np.amin(data[:, 13]))


# In[75]:


# Getting the mean, the max and the min of registered users
print(np.mean(data[:, 14]))
print(np.amax(data[:, 14]))
print(np.amin(data[:, 14]))


# In[76]:


# Mathematical operations on arrays - It is done element by element
arr19 = np.array([10, 20, 30])
arr20 = np.array([1, 2, 3])
print(arr19*arr20)
print(arr19/arr20)
print(arr19**arr20)


# In[78]:


# # Mathematical operations on 2D arrays - It is also done element by element
arr21 = np.array([[10, 20], [30,40]])
arr22 = np.array([[1, 2], [3, 4]])
print(arr21+arr22)


# In[82]:


arr23 = np.array([[10,20], [30, 40]], float)

arr24 = np.sqrt(arr23) # getting the square root of each element
arr25 = np.log10(arr23) # getting the log10 of each element
arr26 = np.rint(arr24)

print (arr24)
print (arr25)
print (arr26)


# In[87]:


# Relational operators on arrays
array1 = np.array([1, 3, 0])
array2 = np.array([1 , 2, 3])

resArray = array1 > array2 # The comparison is done element by element
print(resArray)
print(array1==array2)


# In[89]:


# Array selectors - Arrays permit selection using other arrays
array3 = np.array([45, 3, 2, 5, 67])
boolArr = np.array([True, False, True, False, True])
print(array3[boolArr])


# In[94]:


# Array selectors - Arrays permit selection using other arrays

arr2D = np.array([[45, 3, 67, 34],[12, 43, 73, 36]], float)
boolArr3 = np.array([False, True]) # The False means don't return rows, True means return columns
print (arr2D[boolArr3]) 

arr2D = np.array([[45, 3, 67, 34],[12, 43, 73, 36]], float)
boolArr3 = np.array([[True, False, True, False],[True, True,
False, True]])
print(arr2D[boolArr3])


# In[98]:


# Selecting columns from 2D array using booleans
arr2D = np.array([[45, 3, 67],[12, 43, 73]])
boolArr4 = np.array([True, False, True])
print(arr2D[:,boolArr4])


# In[101]:


# Comparing an array to another then using boolean operator
array4 = np.array([1, 3, 20, 5, 6, 78], float)
array5 = np.array([1, 2, 3, 67, 56, 32], float)
resultArr = array4>array5
print (array4[resultArr])# False, True, True, False, False, True


# In[114]:



casualUsers = np.array(data[:, 13])
registeredUsers = np.array(data[:, 14])

booleansRes = casualUsers>registeredUsers
casUsersMoreThanReg = casualUsers[booleansRes]
percentage = (len(casUsersMoreThanReg)/len(casualUsers))*100
print('Percentage of casual users being more than registered users is {}'.format(percentage))

'''
result = data[:, 13]>data[:, 14]
print ("Percentage of time where causal users > registered ",
(len(data[result])*100.0)/len(data))
'''


# In[116]:


# An array can be compared to a single value
array6 = np.array([1, 3, 0, 2, 4, 5])
resBool = array6>2
resBool1 = array6==2
print(resBool)
print(resBool1)
print('Numbers in the array bigger than 2: {}'.format(array6[resBool]))
print('Numbers in the array equal to 2: {}'.format(array6[resBool1]))


# In[118]:


data = np.array([[1, 2, 3], [2, 4, 5], [4, 5, 7], [6, 2, 3]], float)
print (data)
# return all rows in array where the element at index 1 in a row equals 2
newdata = data[data[:,1] == 2.] # 1 is the column we are checking and : is all the rows
# Then the '== 2' means if that column and row contain 2 
print (newdata)


# In[123]:


data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter = ',')
totalUsers = data[:,15]
holidays = totalUsers[data[:,7] == 0]
notHolidays = totalUsers[data[:,7] == 1]
averageOfUsersOnHolidays = np.mean(holidays)
averageOfUsersNotOnHolidays = np.mean(notHolidays)

print(holidays)
print(notHolidays)
print('Users on holidays {} VS Users not on holidays {}'.format(averageOfUsersOnHolidays, averageOfUsersNotOnHolidays))


# ## Nump Extra PDF 

# In[142]:


# Splitting a 2d array into multiple arrays - Shallow copies of the main array
array7 = np.array([[1, 2, 3], [2, 4, 5], [4, 5, 7], [6, 2, 3]], float)
print(array7)
a,b,c,d = np.split(array7, 4)
print(b)


# In[140]:


# Using hsplit - each of a,b and c get a column from the original array
a,b,c = np.hsplit(array7, 3)
print(a)
#a[1] = 50 # changing the split array changes the original array
#print(array7)


# In[141]:


# Swap the dimensions - rows become columns and columns become rows
a = np.transpose(array7)
print(a)


# In[143]:


# Adding an array at the end of another array
data = np.array([[1, 2, 3], [2, 4, 5], [4, 5, 7], [6, 2, 3]], float)
a = np.array([[21, 0, 2], [1, 4, 15], [3, 9, 2], [3, 4, 6]], float)
c = np.vstack((a,data))
print(c)


# In[147]:


c = np.hstack((a,data))
print(c)


# In[148]:


# Concatenate with axis 0 is similar to vstack
c = np.concatenate((a, data), 0)
print(c)


# In[149]:


# Concatenate with axis 1 is similar to hstack
c = np.concatenate((a, data), 1)
print(c)


# In[153]:


# Matrix determinant
a = np.array([[6,1,1], [4, -2, 5], [2,8,7]])
print(np.linalg.det(a))


# In[159]:


shape2array = np.array([[10, 40],[30, 20]])
# Sort an array along the first axis
firstAxis = np.sort((shape2array), 0)
print(firstAxis)
# Sort an array along the last axis
lastAxis = np.sort((shape2array))
print(lastAxis)
# Make a 2D array flat
flatArray = np.sort(shape2array, None)
print(flatArray)


# In[1]:


'''Write a NumPy program to create a structured
array from given student name, height, class
and their data types. Now sort the array on
height. '''
import numpy as np
data_type = [('name', 'S4'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]
# create a structured array
students = np.array(students_details, dtype=data_type)
print("Original array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))
print(students[0]['name'])


# In[2]:


'''Write a NumPy program to capitalize
the first letter, lowercase, uppercase,
swapcase, title-case of all the
elements of a given array.'''
import numpy as np
x = np.array(['python', 'PHP', 'java', 'C++'], dtype=np.str)
print("Original Array:")
print(x)
capitalized_case = np.char.capitalize(x)
lowered_case = np.char.lower(x)
uppered_case = np.char.upper(x)
swapcased_case = np.char.swapcase(x)
titlecased_case = np.char.title(x)
print("\nCapitalized: ", capitalized_case)
print("Lowered: ", lowered_case)
print("Uppered: ", uppered_case)
print("Swapcased: ", swapcased_case)
print("Titlecased: ", titlecased_case)


# In[9]:


# datetime64 function
a = np.datetime64('2019-03-21T13:22:23')
b = np.datetime64(a,'D')
print(b)


# In[10]:


'''Write a NumPy program to display all the dates for
the month of March, 2017'''
import numpy as np
print("March, 2017")
print(np.arange('2017-03', '2017-04', dtype='datetime64[D]'))


# In[15]:


'''Write a NumPy program to get the dates of yesterday,
today and tomorrow.'''
import numpy as np
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D’)
print("Yestraday: ",yesterday)
today = np.datetime64('today', 'D’)
print("Today: ",today)
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D’))
print("Tomorrow: ",tomorrow)
np.random.randn


# ## not, and , or operators
# Operator Precedence
# not High
# and Medium
# or Low

# In[16]:


""" (1)
If salary more than 40 and you are older than 25 or if you have worked
25 years and have kid you can apply for mortgage.
"""
salary40 = False
age25 = False
work25 = True
kid = True
def state1_1(salary40, age25, work25, kid):
    if salary40 and age25 or work25 and kid:
        print("yes")
    else:
        print("no")
def state1_2(salary40, age25, work25, kid):
    if (salary40 and age25) or (work25 and kid):
        print("yes")
    else:
        print("no")
    
""" (2)
If salary more than 40 or you are older than 35 and if you have worked
10 years or you have kid you can apply for mortgage.
"""
salary40 = False
age35 = False
work10 = True
kid = True
def state2_2(salary40, age35, work10, kid):
    if (salary40 or age35) and (work10 or kid):
        print("yes")
    else:
        print("no")


# ## Logic

# In[ ]:


Write the equivalent expressions to each of the following logic expressions in python:
1. A or B and C or D
2. A or B or C and D
3. A or B or C and D or E
4. not A and B or not C and D
5. A and B or not C
Solution:
1. A or D or (B and C)
2. A or B or (C and D)
3. A or B or E or (C and D)
4. ((not A) and B) or ((not C) and D)
5. (A and B) or (not C)


# ## Recursion

# In[18]:


'''
Recursive functions:
1. Write a function that calculates the 𝑛"# Fibonacci number without using any type of
loop.
2. Write a function that determine if a number is a prime number without using any
type of loop.
'''
# Solution:
# (1)

def fib(n):
    if n < 2:
        return
    else:
        return fib(n - 1) + fib(n - 2);
# (2)

def prime(n, i):
    if (n <= 2):
        return True
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
    return prime(n, i + 1)


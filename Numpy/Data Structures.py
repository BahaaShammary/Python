#!/usr/bin/env python
# coding: utf-8

# In[ ]:


mylist = [1, 2, 3, 4 ,1, 2, 50]


# In[ ]:


print(mylist[len(list)-1])


# In[ ]:


for i in range(1, 10, 2):
    print(i)


# In[ ]:


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# In[ ]:


days.insert(5, 'Bunday')


# In[ ]:


mid_days = days[2:5]
print(mid_days)


# In[ ]:


print(days)


# In[ ]:


del days[5]


# In[ ]:


print(days)


# In[ ]:


nums = [1, 2, 3, 2, 1]
nums.remove(1) # Removes the first occurance of the specified item
print(nums)
nums.sort() # Sorts list in ascending order
print(nums)
nums.reverse() # sorts list in ascending order
print(nums)


# In[ ]:


list1 = [10, 20, 30, 40]
list2 = list1 # list2 will reference the same memory location as list1 so changing list2 changes list1 as well
# double each value in list 2
for counter in range(len(list2)):
    list2[counter] = list2[counter]*2
print (list1)
print (list2)


# In[ ]:


list1 = [10, 20, 30, 40]
list2 = [] + list1 # This means if we change list2, list1 remains the same, you could also loop through list1 and append to list2
# double each value in list 2
for counter in range(len(list2)):
    list2[counter] = list2[counter]*2
print (list1)
print (list2)


# In[ ]:


def main ( ) :
    numbers = [23, 34, 53]
    changeValues(numbers) # When passing a list to another method, and changing something in the list, the list is changed everywhere else
    print ('In Main: ', numbers)

def changeValues(allNums):
    allNums[0] = 0
    print ('In changeValue : ',allNums) 

main()


# In[ ]:


def main():
    number = 5
    changeValue(number)
    print ('In Main: ',number)

def changeValue(num):
    num = 0
    print ('In changeValue: ',num)

main()


# In[ ]:


myName = 'Bahaulddin Ahmad Shammary'
names = myName.split(' ') # Using split
print(names)
print(names[0])
print(names[2])


# In[ ]:





# In[ ]:


userInput = input('Please enter a sentence: ')
tokens = userInput.split(' ')
counter = 0
for word in tokens:
    if len(word) <= 3:
        print(word)
        counter+=1
print('There were {} words with 3 or less characters'.format(counter))
        


# In[5]:


# Dictionaries: 
details = {'Bahaa' : 'Software Development', 'Brian' : 'IT Management', 'Cian' : 'Web Development'}
if 'Bahaa' in details:
    print(details['Bahaa'])


# In[6]:


details['Kevin'] = 'Systems'


# In[7]:


print(details['Kevin'])


# In[ ]:


# Number of elements in a dictionary
print(len(details))


# In[2]:


user = int(input('How many students\' detials would you like to enter? '))
students = {}
for i in range(user):
    studentID = input('What is the student\'s ID')
    studentGrade = int(input('What is the student\'s grade?'))
    
    students[studentID] = studentGrade
print(students)

user2 = input('Enter student ID of student you want to see his/her result')
if user2 in students:
    print('Studnet {} has received {}'.format(user2, students[user2]))
else:
    print('Entered wrong student ID')


# In[8]:


del details['Kevin']; # remove entry with key 'Name'


# '''
# § clear method: deletes all the elements in a dictionary, leaving it empty
# - Format: dictionary.clear()
# § keys method: returns all the dictionary’s keys as a list
# – Format: dictionary.keys()
# § values method: returns all the values in the dictionary as a list
# – Format: dictionary.values()
# – Use a for loop to iterate over the values
# 
# § A dictionary is a mutable data structure and as such it behaves in
# the same way as a list when used with functions.
# § In other words any change made to a dictionary parameter in a
# function is reflected in the original argument
# 
# **clear method: deletes all the elements in a dictionary, leaving it empty
# 
# § Format: dictionary.clear()
# § get method: gets a value associated with specified key
# from the dictionary
# § Format: dictionary.get(key, default)
# § default is returned if key is not found
# § Alternative to [] operator
# § Cannot raise KeyError exception
# 
# '''

# *Sets
# - All items must be unique. No two elements can have the same
# value.
# - Set is unordered
# - Elements can be of different data types
# - add method: adds an element to a set
# - update method: adds a group of elements to a set
# - Single argument must be iterable element, and each of the elements is added to the set
# - remove : remove the specified item from the set
# - The item that should be removed is passed to method as an argument
# - clear method: clears all the elements of the set

# In[9]:


set1 = set()
set1.add("Hello")
set1.update("There")
print (set1)


# In[10]:


set1 = set()
set1.update([1, 2, 10, 20, 43, 2])
for num in set1:
    print (num)


# To find the union of two sets:
# – Use the union method
# § Format: set1.union(set2) or set1 | set2
# § Returns a new set which contains the union of both sets
# § Intersection of two sets: a set that contains only the elements
# found in both sets
# § Use the intersection method
# § Format: set1.intersection(set2) or set1 & set2

# In[11]:


set1 = set([1, 2, 3, 4])
set2 = set([4, 5, 6])
set3 = set([4, 7, 8, 9])
set4 = set1 | set2 | set3
print (set4)
set5 = set1 & set2 & set3
print (set5)


# Difference of two sets: a set that contains the elements that
# appear in the first set but do not appear in the second set
# § To find the difference of two sets:
# § Use the difference method
# § Format: set1.difference(set2)
# § Use the - operator
# § Format: set1 - set2

# In[ ]:





# In[12]:


set1 = set([1, 2, 3, 4])
set2 = set([4, 5, 6])
difference = set1 - set2;
print (difference)


# In[16]:


more = True
dict = {}

while(more):
    surname = input('Please enter the surname of the employee ')
    salary = float(input('Please enter {}\'s salary '.format(surname)))
    dict[surname] = salary
    
    keepGoing = input('Would you like to keep going?(yes/no)')
    if keepGoing == 'no':
        more = False
    else:
        more = True
# printing the total salary bill for the company through the use of the dictionary:
total = 0
for key in dict:
    total+= dict[key]
    
print('The total salary is {}'.format(total))


# In[17]:


print(dict)


# In[19]:


dict['kevin'] = 45000
print(dict.values())
print(set(dict.values()))


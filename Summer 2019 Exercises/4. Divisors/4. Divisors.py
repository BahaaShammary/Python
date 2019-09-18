#!/usr/bin/env python
# coding: utf-8

# **Exercise 4
# 
# *Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
# 
# The topics that you need for this exercise combine lists, conditionals, and user input. There is a new concept of creating lists.
# 
# There is an easy way to programmatically create lists of numbers in Python.
# 
# To create a list of numbers from 2 to 10, just use the following code:
# 
#   x = range(2, 11)
# Then the variable x will contain the list [2, 3, 4, 5, 6, 7, 8, 9, 10]. Note that the second number in the range() function is not included in the original list.
# 

# In[6]:


num = int(input('Please enter a number to show all its divisors: '))
x = [i for i in range(2, num)]
#print(x)


# In[8]:


list_of_divisors = [n for n in x if num % n == 0]
print(list_of_divisors)


#!/usr/bin/env python
# coding: utf-8

# **Exercise 11
# 
# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
# 
# Concepts:
# 
# Functions
# Reusable functions
# Default arguments

# In[7]:


def getUserInput():
    user_input = int(input('Please enter a number to see if it is a prime or not: '))
    return user_input


# In[9]:


def checkPrime(number):
    prime = False
    x = [i for i in range(2, number)]
    list_of_divisors = [n for n in x if number % n == 0]
    if len(list_of_divisors) == 0:
        prime = True
    else: 
        prime = False
    return prime


# In[15]:


'''Calling the methods above from here '''
num = getUserInput() # First get the user input
prime_num = checkPrime(num) # Then pass user input as a parameter to check if it is prime or not
if prime_num == False:
    print('The number', num, 'is not Prime')
else:
    print('The number', num, 'is Prime')


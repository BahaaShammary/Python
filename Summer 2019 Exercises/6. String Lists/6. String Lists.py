#!/usr/bin/env python
# coding: utf-8

# **Exercise 6 
# 
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
# 
# A convenient way to get sublists between two indices:
# 
#   >>> a = [5, 10, 15, 20, 25, 30, 35, 40]
#   >>> a[1:4]
#  
# You can also include a third number in the indexing, to count how often you should read from the list:
# 
#   >>> a = [5, 10, 15, 20, 25, 30, 35, 40]
#   >>> a[1:5:2]
#   [10, 20]
#   >>> a[3:0:-1]
#   [15, 10, 5]
#   
# Because strings are lists, you can do to strings everything that you do to lists. You can iterate through them:
# 
#   string = "example"
#   for c in string: 
#     print "one letter: " + c
# Will give the result:
# 
#   one letter: e
#   one letter: x
#   one letter: a
#   one letter: m
#   one letter: p
#   one letter: l
#   one letter: e

# In[27]:


user_input = input('Please enter a word: ')

reverse_user_input = user_input[::-1]

if (user_input.islower() == reverse_user_input.islower()) is True: # Used islower() so Capital letters don't get in the way
    print('The word you entered is a palindrome')
elif (user_input.islower() == reverse_user_input.islower()) is False:
    print('The word you entered is not a palindrome')


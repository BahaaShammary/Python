# Name: Bahaulddin Shammary
# Date: 08/06/2019

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(my_list)
num = int(input("Please enter a number to see all the smaller numbers from the above list: "))
list_of_nums = []

# Doing it the long way
'''
for i in my_list:
    if i < num:
#         print(i)
        list_of_nums.append(i)
'''

# Using List Comprehension
list_of_nums = [i for i in my_list if i < num]

print(list_of_nums)

#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv


# In[5]:


fileObj = open("bikeSharing.csv")
sumWind = 0
numOfRows = 0
for line in fileObj:
    lineContents = line.split(',')
    sumWind += float(lineContents[12])
    numOfRows += 1
    
print ("Average is ", ((sumWind*67)/numOfRows))


# In[1]:


import numpy as np


# with open('bikeSharing.csv') as a_file:
#     data = csv.reader(a_file)
#     arr = np.array[data]
#     for i in data:
#         print(i[15])
#         if i == 12:
#             break

# In[4]:


with open('bikeSharing.csv') as a_file:
    data = csv.reader(a_file)
    list = [i[15] for i in data] # list comprehension
    arr = np.array(list, int)
    
print(arr)


# In[29]:


my_data = np.genfromtxt('bikeSharing.csv', delimiter=',', dtype=None)
print(my_data[0])


# ## Question 1 (i) 
# > Average total users on days that are holidays VS Average total users on days that are not
# 

# In[10]:


data  = np.genfromtxt("bikeSharing.csv", delimiter = ',', dtype=float)
# Number of users is on column 15
# Column Number 5 for holidays
users = np.copy(data[:,15])
holidayData = users[data[:, 5] == 0]
noHolidayData = users[data[:, 5] == 1]
avgHoliday = np.mean(holidayData)
avgNotHoliday = np.mean(noHolidayData)
print('Holiday value: 0\nMean number of users: {}'.format(avgHoliday))
print('Holiday value: 1\nMean number of users: {}'.format(avgNotHoliday))


# ## Question 1 (ii)

# In[8]:


tempArray = np.copy(data[:, 9])
realTempArray = tempArray*41
realTempArray


# # Question 1 (iii)

# In[13]:


casualUsers = np.copy(data[:, 13])
boolArray = casualUsers > data[:, 14]
percentage = (len(casualUsers[boolArray])/len(casualUsers))*100
perc


# ## Question 1 (iv)
# For each of the
# 4 possible weather conditions calculate the average number of rental bikes.

# In[27]:


# Weather conditions column 8
# Number of rental bikes column 15
weatherDict = {1: 'Clear', 2: 'Misty', 3: 'Light Rain', 4: 'Heavy Rain'}
rentalBikes = np.copy(data[:,15]) 
'''
clear = np.mean(rentalBikes[data[:, 8] == weatherDict['Clear']])
misty = np.mean(rentalBikes[data[:, 8] == weatherDict['Misty']])
lightRain = np.mean(rentalBikes[data[:, 8] == weatherDict['Light Rain']])
heavyRain = np.mean(rentalBikes[data[:, 8] == weatherDict['Heavy Rain']])
print('Mean users for weather = Clear : {}'.format(clear))
print('Mean users for weather = Misty : {}'.format(misty))
print('Mean users for weather = Light Rain : {}'.format(lightRain))
print('Mean users for weather = Heavy Rain : {}'.format(heavyRain))
'''
for key in weatherDict:
    avg = np.mean(rentalBikes[data[:, 8] == key])
    print('Mean users for weather = {} : {}'.format(weatherDict[key], avg))


# ## Question 1 (v)
# Work out the average number of casual users for the following
# temperature ranges:
# 1, 5
# 6, 10
# 11, 15
# 16, 20
# 21, 25
# 26, 30
# 31, 35
# 36, 40

# In[29]:


# Casual users column 13 
# Temp column is 9
def analyseTemp(data, minValue, maxValue):
    # the temperature values stored in the array are multiplied by 41 
    
    higherTempCondition = (data[:,9]*41)>=minValue  # Getting a boolean array of values more than 1  
    lowerTempCondition = (data[:,9]*41)<=maxValue  # But also getting boolean array of values less than 5
    
    subset = data[higherTempCondition & lowerTempCondition] # Getting all the data that are between the min and max

    meanValue = np.mean(subset[:, 15]) # Getting the mean of users using the data we got previously
    print ("For temp in range ", minValue, "to", maxValue, "the mean number of casual users was ", meanValue)

for temp in range(1, 40, 5):
    analyseTemp(data, temp, temp+4)


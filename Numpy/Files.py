#!/usr/bin/env python
# coding: utf-8

# In[8]:


file_object = open('text.txt', 'w')
file_object.write('Hello World \nI am Bahaulddin')
file_object.close()


# In[11]:


file_object = open('text.txt', 'r')
read_file = file_object.read()
file_object.close()
print(read_file)


# In[13]:


file_object = open('text.txt', 'r')
read_file = file_object.readline()
file_object.close()
print(read_file)


# In[15]:


# Writing to a file using loop

def main() :
    salesFile = open('sales.txt', 'w')
    numDays = 5
    for count in range( 1, numDays + 1 ) :
    # Get the sales for a day.
        sales = int(input( 'Enter the sales for day ' + str(count) + ': '))
        salesFile.write(str(sales) + '\n')
    salesFile.close()

main()


# In[17]:


# Looping over each line in the file and printing it
def main():
    sales_file = open('sales.txt', 'r')
    line = sales_file.readline()
    
    while line != '':
        print(line)
        line = sales_file.readline()

    sales_file.close()

main()


# In[19]:


# Using a for loop to print file contents (Better than while loop)

def main():
    sales_file = open('sales.txt', 'r')
    
    for line in sales_file:
        print(line.rstrip('\n')) # Using rstrip to remove the \n to get rid of spaces like in the above output

    sales_file.close()

main()


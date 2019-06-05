# Name: Bahaulddin Shammary
# Date: 05/06/2019



name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
ageToReach = 100
currentYear = 2019
message = "\n" + name + ", you will reach " + str(ageToReach) + " in the year " + str(currentYear+(ageToReach-age))
print(message)

num = int(input("Please enter another number: "))
for x in range(num):
    print(message)

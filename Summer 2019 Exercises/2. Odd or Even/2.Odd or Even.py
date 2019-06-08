# Name: Bahaulddin Shammary
# Date: 08/06/2019


def get_num():
    num = int(input("Hi! Please enter a number: "))
    if (num % 2) == 0:
        print("This number {} is an even number".format(num))

    elif (num % 2) > 0:
        print("This number {} is an odd number".format(num))

    return num


def multiple_of_four(number):
    if number % 4 == 0:
        print("The number you entered is also a multiple of 4")


def get_two_numbers():
    num = int(input("\nPlease enter a new number: "))
    check = int(input("\nPlease enter another number to divide by: "))

    if num % check == 0:
        print("The number {} divides evenly by {}".format(num, check))

    elif num % check == 1:
        print("The number {} does not divide evenly by {}".format(num, check))


def main():
    num = get_num()
    multiple_of_four(num)
    get_two_numbers()


main()

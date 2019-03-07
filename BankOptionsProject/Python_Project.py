# Author : Bahaulddin Shammary
# Subject: Python Project

from random import randrange  # This is used later to create new bank account numbers
import validation_code


def reading_file():  # 1.
    data_file = open('bank.txt')  # opening the file
    raw_list_of_data = data_file.readlines()  # reading the contents of the file and assigning them to a list
    clean_list_of_data = []
    for i in raw_list_of_data:  # looping through the raw list and doing a specific thing to it
        item = i.rstrip('\n')  # Removing the new line, and putting it back later when writing to file
        clean_list_of_data.append(item)
    data_file.close()  # closing the file
    return clean_list_of_data  # returning the list of the data read from the file


def splitting_list(list_of_data):  # 2. This func turns the list of data into 4 lists each contains different info
    # Using list comprehension to cut down on how many lines used for the loops
    account_no = [(i.split(' '))[0] for i in list_of_data]  # This list is for bank account numbers
    deposit = [(i.split(' '))[1] for i in list_of_data]  # This list is for the amounts deposited in the bank by users
    f_name = [(i.split(' '))[2] for i in list_of_data]  # This list stores the first name of the account holder
    l_name = [(i.split(' '))[3] for i in list_of_data]  # This list stores the last name of the account holder
    return account_no, deposit, f_name, l_name  # returning the four lists containing the data


def display_user_options():  # 3. This func prints the options for the user to choose from
    print('WELCOME TO OUR BANK - Would you like to:\n1. Open an account\n2. Close an account\n3. Withdraw money\n4. '
          'Deposit Money\n5. Generate a report for management\n6. Quit\n')


def user_choice():  # 4. This func has an input for the user and returns the user's choice
    users_choice = validation_code.read_nonnegative_integer_menu('Choose a number from the above options please: ')
    return users_choice


def write_to_file(account_num_list, deposit_list, firstname_list, lastname_list):  # func for writing to file
    data_file = open('bank.txt', 'w')  # opening the file and adding to it the new information
    for i, x in enumerate(account_num_list):  # This helps loop through all items in the list and write them to file
        data_file.writelines(str(x) + ' ' + str(deposit_list[i]) + ' ' + firstname_list[i] + ' ' + lastname_list[i] +
                             '\n')
    data_file.close()  # closing the opened file


def lines():
    print('=' * 60)


def open_account(account_num_list, deposit_list, firstname_list, lastname_list):  # 6. This func opens a new account
    something_is_wrong = True
    user_random_account_no = 0
    while something_is_wrong:
        user_random_account_no = randrange(100000, 999999)  # a new bank account number is created using random range func
        if str(user_random_account_no) in account_num_list:  # this is to check if account number already exists
            something_is_wrong = True  # if it dies, then get another random number by looping again
        else:
            something_is_wrong = False  # of the random account number is unique, then continue through the program
    deposit_input = validation_code.read_nonnegative_float('Please enter the amount you would like to deposit: ')
    firstname_input = validation_code.read_nonempty_alphabetical_string('What is your first name ? ')  # get user name
    lastname_input = validation_code.read_nonempty_string('What is your last name? ')  # asking the user for last name
    account_num_list.append(str(user_random_account_no))
    deposit_list.append(deposit_input)
    firstname_list.append(firstname_input)
    lastname_list.append(lastname_input)
    write_to_file(account_num_list, deposit_list, firstname_list, lastname_list)
    lines()
    print('The following details of the account have been added:')
    print('Account no.\t Balance\t Full name')
    print(user_random_account_no, '\t\t', deposit_input, '\t', firstname_input, lastname_input)
    lines()


def close_account(account_num_list, deposit_list, firstname_list, lastname_list):  # 8. This func deletes an account
    account_number = validation_code.read_nonnegative_integer('Please enter the number of the account you would like to'
                                                              ' close: ')
    # Asking user to input the account number, and it is validated to only accept 5 digits
    if str(account_number) in account_num_list:  # This condition checks if the account number exists in the file
        get_index_of_account_no = account_num_list.index(str(account_number))  # get the position of the account number
        deposit_of_account_number = deposit_list[get_index_of_account_no]  # get the deposit of the same acc no position
        firstname_of_account_number = firstname_list[get_index_of_account_no]  # get the name of same position as acc no
        lastname_of_account_number = lastname_list[get_index_of_account_no]  # get lastname of same position as acc no
        del account_num_list[get_index_of_account_no]  # I just delete the index and it deletes the intended account no.
        del deposit_list[get_index_of_account_no]  # I just delete the index and it deletes the intended balance.
        del firstname_list[get_index_of_account_no]  # I just delete the index and it deletes the intended first name.
        del lastname_list[get_index_of_account_no]  # I just delete the index and it deletes the intended last name.
        write_to_file(account_num_list, deposit_list, firstname_list, lastname_list)  # call the func to write to file
        lines()
        print('The following account is deleted: ', account_number, deposit_of_account_number,
              firstname_of_account_number, lastname_of_account_number)  # A confirmation for user on the screen
        lines()
    else:  # if user inputs an invalid account number, then he is informed of it
        lines()
        print('There is no such account number registered with the bank')
        lines()


def withdraw_money(account_num_list, deposit_list, firstname_list, lastname_list):  # 9. Function for withdrawing money
    account_number = validation_code.read_nonnegative_integer('Please enter the account number you would like to draw '
                                                              'money from: ')
    # Re-using the function of user input for account number that is used previously in close_account() function.
    something_is_wrong = True
    while something_is_wrong:  # in case user does not have enough balance, he can retry and enter a different amount
        if str(account_number) in account_num_list:  # checking if account number is in the account number list
            index_of_account_number = account_num_list.index(str(account_number))  # position of account number in list
            user_deposit = deposit_list[index_of_account_number]  # storing user's deposit in a variable for later use
            user_firstname = firstname_list[index_of_account_number]  # storing user's first name in a variable
            user_lastname = lastname_list[index_of_account_number]  # storing user's last name in a variable
            lines()
            print('Account details:', account_number, user_deposit, user_firstname, user_lastname)  # display info
            lines()
            amount_to_withdraw = validation_code.read_nonnegative_float('How much would you like to withdraw from your '
                                                                        'account ' + user_firstname + '? ')  # withdraw
            if float(user_deposit) >= amount_to_withdraw:  # checking if the amount withdrawn is not bigger than balance
                user_deposit = float(user_deposit) - amount_to_withdraw  # deducting the amount requested by user
                deposit_list[index_of_account_number] = user_deposit  # changing the user's balance on the final list
                lines()
                print('Updated account details: ', account_number, user_deposit, user_firstname, user_lastname)
                lines()
                write_to_file(account_num_list, deposit_list, firstname_list, lastname_list)
                something_is_wrong = False
            else:
                lines()
                print('You have insufficient funds')  # telling user what's wrong
                lines()
                more = validation_code.read_nonempty_string('Would you like another attempt to enter a different amount'
                                                            ' (Y/N)? ')
                # asking user if they would like to withdraw a different amount for the same account
                if more.upper() == 'Y' or more.startswith('y') or more.startswith('Y'):
                    something_is_wrong = True
                else:
                    something_is_wrong = False


def deposit_money(account_num_list, deposit_list, firstname_list, lastname_list):
    something_is_wrong = True
    while something_is_wrong:
        account_number = validation_code.read_nonnegative_integer('Enter the account number you would like to deposit '
                                                                  'money into: ')
        # Re-using the function of user input for account number that is used previously in close_account() function.
        if str(account_number) in account_num_list:  # checking if account number is in the file's account number list
            index_of_account_number = account_num_list.index(str(account_number))  # get position of the account number
            user_deposit = deposit_list[index_of_account_number]  # locate user's deposit using the position of acc no.
            user_firstname = firstname_list[index_of_account_number]  # locate first name of user
            user_lastname = lastname_list[index_of_account_number]  # lcoate last name of user
            lines()
            print('Account details:', account_number, user_deposit, user_firstname, user_lastname)  # user's info
            lines()
            amount_to_deposit = validation_code.read_nonnegative_float('How much would you like to deposit into your '
                                                                       'account ' + user_firstname + '? ')  # get balanc
            user_deposit = float(user_deposit) + amount_to_deposit  # adding the user's deposit to his balance
            deposit_list[index_of_account_number] = user_deposit  # updating the list containing the user's deposit
            lines()
            print('Updated account details: ', account_number, user_deposit, user_firstname, user_lastname)
            lines()
            write_to_file(account_num_list, deposit_list, firstname_list, lastname_list)
            something_is_wrong = False  # exit loop
        else:  # if bank account number is wrong, then do the following
            lines()
            print('This account number does not exist')  # notify the user of what's wrong
            lines()
            more = validation_code.read_nonempty_string('Would you like another attempt to enter a different account '
                                                        'number (Y/N)? ')
            # asking user if they would like to try again
            if more.upper() == 'Y' or more.startswith('y') or more.startswith('Y'):  # checking if yes
                something_is_wrong = True  # then loop through again and ask for a new account number
            else:
                something_is_wrong = False  # if not then just exit without doing anything


def management_report(account_num_list, deposit_list, firstname_list, lastname_list):  # 11. report for management func
    if account_num_list == [] or deposit_list == [] or firstname_list == [] or lastname_list == []:
        print('There is no data to display')
        quit_program()
    else:
        lines()
        print('\tREPORT FOR MANAGEMENT\t')  # Title of the report
        print('Account no.\t', 'Deposit\t', 'Full Name')  # to explain the data and show them in a neat manner
        for i, x in enumerate(account_num_list):  # looping through the account numbers list
            print(str(i+1), '.', x, '\t', deposit_list[i], '\t', firstname_list[i], lastname_list[i])  # Print the data
        total = 0  # will add to it each deposit in the bank
        for i in deposit_list:  # looping through the numbers of deposits in the deposit list
            total += float(i)  # every time adding the deposit to the total
        print('\nThe bank has a deposit total of: €', total)  # printing the total
        deposit_list_numbers = [float(num) for num in deposit_list]  # To convert all items to numbers to get max
        highest_deposit = max(deposit_list_numbers)  # getting what the maximum number is in the deposit list
        index_of_highest_deposit = deposit_list_numbers.index(highest_deposit)  # Locate this deposit in deposit list
        print('The following account has the highest deposit in the bank: ')
        print(account_num_list[index_of_highest_deposit], '\t', deposit_list[index_of_highest_deposit], '\t',
              firstname_list[index_of_highest_deposit], lastname_list[index_of_highest_deposit] + '\n')  # and printing
        # the rest of the data with the same location in their lists as the maximum deposit in the list
        lines()


def quit_program():  # 12.  This func asks user if they need to do anything else before quitting program
    something_is_wrong = True
    while something_is_wrong:
        more = validation_code.read_nonempty_string('Do you need to do something else? (Y/N): ')  # checking with user
        # to exit or not
        if more.upper() == 'Y' or more.startswith('y') or more.startswith('Y'):
            main()
            something_is_wrong = False
        else:
            print('Exiting program...')
            something_is_wrong = False


def options(usr_choice, account_no, deposit, firstname, lastname):  # 5. This func matches the user's choice with the
    # relevant functions to do the required task
    if usr_choice == 1:
        print('Open an account...\n')  # confirming user's choice
        open_account(account_no, deposit, firstname, lastname)  # 6. The func creates new account deposit and full name
    elif usr_choice == 2:
        print('Close an account...\n')  # confirming user's choice
        close_account(account_no, deposit, firstname, lastname)  # 7. The func closes an account by removing all
        # associated details with the account num entered by the user
    elif usr_choice == 3:
        print('Withdraw Money...\n')  # confirming user's choice
        withdraw_money(account_no, deposit, firstname, lastname)  # 9. This func amends the deposit list depending on
        # how much the user withdraws from his balance
    elif usr_choice == 4:
        print('Deposit Money...\n')  # confirming user's choice
        deposit_money(account_no, deposit, firstname, lastname)  # 10. This func amends the deposit list depending on
        # how much the user deposits money into his account
    elif usr_choice == 5:
        print('Generating a report for management...\n')  # confirming user's choice
        management_report(account_no, deposit, firstname, lastname)  # 11. This func displays the info for management
    else:
        print('before we quit...')


def main():
        list_of_data = reading_file()  # 1. This func reads the bank.txt file and returns a list of the data in the file
        display_user_options()  # 3. This func displays the options for user to choose from
        choice = user_choice()  # 4. This func asks the user for their choice and returns the user's choice
        account_no, deposit, forename, lastname = splitting_list(list_of_data)  # 2. The func splits the list to 4 lists
        options(choice, account_no, deposit, forename, lastname)  # 5. The func takes user's choice and calls a func
        quit_program()  # 12. This func asks the user if they would like to do something else or exit


main()

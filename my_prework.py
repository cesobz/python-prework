# Question 1: 
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(username):
     print('Enter your name:')
username = input()
print('Hello, ' + username)


# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for i in range (1,100):
        if i % 2 != 0:
            print(i)

first_odds()


# Question 3:
# Please write a Python Function, max_num_in_list to return the max number of a given list.
# THe first line of the code has been defined as below.

def max_num_in_list(a_list):
    maximum = a_list[0]
    for i in range(len(a_list)):
        if a_list[i] > maximum:
            maximum = a_list[i]
    return maximum
a_list = [5,10,15,20,25]
print(max_num_in_list(a_list))

# Question 4
# Write a funvtion to retrun if the given year is a leap year.
# A leap year is divisible by 100, unless it is also diviible by 400.
# The return should be a boolean Type(true/false)

def is_leap_year(a_year):
    if(a_year % 400 == 0):
        return True
    elif(a_year % 100 == 0):
        return False
    elif(a_year % 4 == 0):
        return True
    else:
        return False
a_year =int(2022)
print(is_leap_year(a_year))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers
# but [1,2,4,5] are notconsecutive numbers
# The return should be a bolean type/

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) +1))

a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list = [1,2,4,5]
print(is_consecutive(a_list))

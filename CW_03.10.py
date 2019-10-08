# # Напишіть програму, яка пропонує користувачу ввести ціле число 
# # і визначає чи це число парне чи непарне, чи введені дані коректні.
# try:
#     number=int(input('Enter a number: '))
#     if number<0:
#         raise ValueError 
#     if number%2==0:
#         print('The number is even')
#     if number%2==1:
#         print('The number is odd') 
# except ValueError:
#     print('Enter a positive number')

# n = input("Input entire number: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("\n You entered incorrect data!\n")
#         n = input("Input entire number:\n ")
# if n % 2 == 0:
#     print("{0} is the even number.".format(n))
# else:
#     print("{0} is the odd number.".format(n))

# Напишіть програму, яка пропонує користувачу ввести свій вік, 
# після чого виводить повідомлення про те чи вік є парним чи непарним числом. 
# Необхідно передбачити можливість введення від’ємного числа, 
# в цьому випадку згенерувати власну виняткову ситуацію. 
# Головний код має викликати функцію, яка обробляє введену інформацію

# def check_age (age):
#     try:
#         if age<0:
#             raise ValueError
#     except ValueError:
#         return ('Enter a positive number')
#         if age % 2 == 0:
#             return "{0} is the even number.".format(age)
#         else:
#             return "{0} is the odd number.".format(age)
        

# age=int(input('What is your age? '))    

# print(check_age (age))

# '''This program calculates the ratio of two numbers entered by the user sequentially 
# and separated by a comma (division by zero, syntactic errors, and other exceptions considered. 
# Use else та finally.'''

# try:
#     nums=input('Give two numbers separated by a comma: ')
#     li=(nums.split(','))
#     result=float(li[0])/float(li[1])
# except ZeroDivisionError:
#     print ('Cannot divide by zero.')
# except ValueError:
#     print ('Please enter numbers separated by comma like this: 1, 2.')
# else:
#     print (result)
# finally:
#     print ('Thank you!')

'''This program analyses the input number and produces the day of the week. Exceptions: numbers 8+, 
chars other than digits'''
try:
    num=int(input('Give a number between 1 and 7: '))
    if num==1:
        print ('Monday')
    elif num==2:
        print ('Tuesday')
    elif num==3:
        print ('Wednesday')
    elif num==4:
        print ('Thirsday')
    elif num==5:
        print ('Friday')
    elif num==6:
        print ('Saturday')
    elif num==7:
        print ('Sunday')
    elif num>7:
        raise ValueError
except ValueError:
    print ('Enter a number between 1 and 7 including.')
finally:
    print ('Thank you.')




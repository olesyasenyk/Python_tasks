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

nums=input('Give two numbers separated by a comma: ')

try:
    a=(nums[0])
    b=(nums[2])
    if a is tystr:
        raise TypeError
    else:

    #     
    # if b==0.0:
    #     raise ValueError

#     elif nums[2] is not float:
#         raise TypeError
# except TypeError:
#     print('Not a number')
    # else:
    #     print (a/b)
# except ValueError:
#     print('Division by zero')
except TypeError:
    print('Not a number')
finally:
    print('Thank you')




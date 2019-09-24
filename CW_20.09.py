# def mean(*args):
#     suma=0
#     for i in range(len(args)):
#         suma=suma+args[i] 
#     return suma/len(args)    

# def arithmetic_mean(*args):
#     return sum(args)/len(args)

# print(mean(1,3,6,7))

# def absolute (n):
#     if n>0:
#         return n
#     else:
#         return -n

# print (absolute(-4))

# def search_bigger (a,b):
#     if a>b:
#         return a
#     else:
#         return b

# print(search_bigger(4,8))

# Написати програму, яка обчислює площу прямокутника, 
# трикутника та кола (написати три функції для обчислення площі, 
# і викликати їх в головній програмі в залежності від вибору користувача)

# def rectangle():
#     a=float(input('Input width: '))
#     b=float(input('Input length: '))
#     print('Suare={}'.format (a*b))

# def triangle():
#     a=float(input('Input basis: '))
#     h=float(input('Input height: '))
#     print('Suare={}'.format (a*h/2))

# def circle():
#     PI=3.14
#     r=float(input('Input raius: '))
#     print('Suare={}'.format (PI*r**2))

# figure=input('What figure do you need the area of? ')
# if figure.lower()=='rectangle':
#     rectangle()
# elif figure.lower()=='triangle':
#     triangle()
# elif figure.lower()=='circle':
#     circle()
# else:
#     print ("I don't know how to count that")

#Написати функцію, яка обчислює суму цифр введеного числа.
# def calculate_sum (a):
#     a=str(a)
#     #a=list(a)
#     # for x in range(len(a)):
#     #     a[x]=int(a[x])
#     a=[int(a[x]) for x in range(len(a))]
#     return sum(a)

# print (calculate_sum(35))

# Написати програму калькулятор, яка складається з наступних функцій: 
# головної, яка пропонує вибрати дію та додаткових, 
# які реалізовують вибрані дії, калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, після виходу, 
# користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

def add_numbers ():
    a=float(input('Input first number: '))
    b=float(input('Input second number: '))
    print ('The sum is {}.'.format(a+b))
def subtract_numbers ():
    a=float(input('Input first number: '))
    b=float(input('Input second number: '))
    print ('The difference is {}.'.format(a-b))
def multiply_numbers ():
    a=float(input('Input first number: '))
    b=float(input('Input second number: '))
    print ('The product is {}.'.format(a*b))
def divide_numbers():
    a=float(input('Input first number: '))
    b=float(input('Input second number: '))
    print ('The ratio is {}.'.format(a/b))
while True:    
    operation=input('Select operation: 1-add, 2-subtract, 3-multiply, 4-divide, 5-quit: ')
    if operation=='1':
        add_numbers()
    elif operation=='2':
        subtract_numbers()
    elif operation=='3':
        multiply_numbers()
    elif operation=='4':
        divide_numbers()
    elif operation=='5':
        print ('Thanks for using my calculator!')
        break
    else:
        print('Error')



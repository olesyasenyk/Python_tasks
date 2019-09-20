#1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.
number=int(input('How many numbers in the list?: '))
num_list=[]
for i in range(number):
    element=int(input('Please give a number: '))
    num_list.append(element)
print(num_list)
max=num_list[0]
min=num_list[0]
for x in range(number):
    if num_list[x]>max:
        max=num_list[x]
    if num_list[x]<min:
        min=num_list[x]
print("Maximum number = {}. Minimum number = {}.".format(max, min))
    
#2.  В інтервалі від 1 до 10 визначити числа 
#•  парні, які діляться на 2,
#•  непарні, які діляться на 3, 
#•  числа, які не діляться на 2 та 3.
for i in range(1,10):
    if i%2==0:
        print (i,'is an even number that is a multiple of 2.')
    elif i%3==0:
        print (i,'is an odd number that is a multiple of 3.')
    else:
        print (i,'is a number that is a multiple of neither 2 nor 3.')

#3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)
n=int(input('Number: '))
total=1
for i in range(1, n+1):
    total=total*i
print (total)

#4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
#Якщо логін вірний (First), то привітайте користувача. 
#Якщо ні, то виведіть повідомлення про помилку. 
#(використайте цикл while)
login=input('Login: ')
check='First'
i=0
while i<len(login):
    if len(login)!=len(check):
        print('Wrong login')
        break
    elif login[i]!=check[i]:
        print('Wrong login')
        break
    i+=1
else:
    print('Login correct')

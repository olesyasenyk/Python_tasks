#1.Роздрукувати всі парні числа менші 100 (while; for).
for i in range(0,100,2):
    print (i, end=' ')

i=0
while i<100:
    if i%2==0:
        i+=2
        print (i, end=' ')

#2.Роздрукувати всі непарні числа менші 100. (continue; без continue)
for i in range(100):
    if i%2==0:
        continue
    print (i, end=' ')

print (list(range(1,100,2)))

#3.Перевірити чи список містить непарні числа (використати оператор break)
spisok=[1,2,3,4,5,6]
contain_odd=False
for item in spisok:
    if not item % 2 ==0:
        contain_odd=True
        break
if contain_odd:
    print ('There is an odd number in the list')
else:
    print ('There are only even numbers in the list')

#4.Створити список, який містить елементи цілочисельного типу,
#потім за допомогою циклу перебору змінити тип даних елементів
#на числа з плаваючою крапкою. (використати float ()).
spisok=[5,6,7,8]
for i in range (len(spisok)):
    spisok[i]=float(spisok[i])
print(spisok)

#5.Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли.
#(Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
n=input('Enter a number: ')
n=int(n)
a=0
b=1
print (a,b,end=' ')
while a<n:
    a=a+b
    b=b+a
    print (a,b,end=' ')
    if b==n:
        break

#6.Створити список, що складається з чотирьох елементів типу string.
#Потім, за допомогою циклу for, вивести елементи по черзі на екран.
spisok=['olesia','max','olga','mykola']
for i in spisok:
    print(i)
    
#Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі додавався певний символ, наприклад “#”. 
#(Підказка: цикл for може бути вкладений в інший цикл, а також  треба використати функцію print(“ ”, end=”%”)).
spisok=['olesia','max','olga','mykola']
for i in spisok:
    for l in i:
        print(l, end='#')
        
#7.Юзер вводить число з клавіатури, написати скріпт, який визначає чи це число просте чи складне.
while True:
    number=int(input('Number: '))
    if number%2==0 and number!=2 or number%3==0 and number!=3:
        print ('composite number')
    else:
        print ('simple number')

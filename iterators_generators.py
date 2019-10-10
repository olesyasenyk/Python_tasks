# # Спробуйте переписати наступний код через map. 
# # Він приймає список реальних імен і замінює їх хеш-прізвищами, 
# # використовуючи  більш надійний метод-хешування.

# # names = ['Sam', 'Don', 'Daniel'] 
# # for i in range(len(names)): 
# #     names[i] = hash(names[i]) 
# # print(names) 

# # # => [6306819796133686941, 8135353348168144921, -1228887169324443034]

# names = ['Sam', 'Don', 'Daniel']
# hash_names = list(map(hash, names)) # list is necessary!!!!!
# print (hash_names)

##Вивести список кольору “red”, який найчастіше зустрічається в даному списку  
# [“red”, “green”, “black”, “red”, “brown”, “red”, “blue”, “red”, “red”, 
# “yellow” ] використовуючи функцію filter.

# l=['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red', 'red', 'yellow']
# def is_red(string):
#     if string=='red':
#         return string
# result = filter(is_red, l) 

# print (list(result))

# Всі ці числа в списку мають стрічковий тип даних, наприклад  
# [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список, всі 
# числа якого мають тип даних integer:
# 1)  використовуючи метод  append
# 2)  використовуючи метод  map

# li=['1', '2', '3', '4', '5', '6', '7']
# li1=[]
# for e in range(len(li)):
#     li1.append(int(li[e]))
# print (li1)

# li = ['1', '2', '3', '4', '5', '6', '7']
# li1 = list(map(int, li)) # list is necessary!!!!!
# print (li1)

# Перетворити список, який містить милі,  в список, який містить кілометри 
# (1 миля=1.6 кілометра)
#   a) використовуючи функцію map
#   b) використовуючи функцію map та lambda

# li = [12, 26, 98, 550]
# def to_miles (km):
#     return round(km*1.6)
# li1=list(map(to_miles, li))
# print (li1)

# li = [12, 26, 98, 550]
# li1=list(map(lambda km: round(km*1.6), li))
# print(li1)

## Знайти найбільший елемент в списку  використовуючи функцію reduce
# from functools import reduce
# li = [12, 26, 98, 550]
# def bigger_number (a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(reduce(bigger_number, li, 0))

##Перепишіть наступний код, використовуючи map, reduce і filter. 
## Filter приймає функцію і колекцію. Повертає колекцію тих елементів, 
## для яких функція повертає True.
people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 
height_total = 0 
height_count = 0 
for person in people: 
    if 'height' in person: 
        height_total += person['height'] 
        height_count += 1 
print(height_total)
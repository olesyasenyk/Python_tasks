number=input('Please give a 4-digit number: ')
print('The product of its digits is:', int(number[0])*int(number[1])*int(number[2])*int(number[3]))
print('The reverse order of its digits is:', number[3],number[2],number[1],number[0])
list_of_numbers=[int(number[0]),int(number[1]),int(number[2]),int(number[3])]
list_of_numbers.sort()
print('Let us sort the gidigs:',list_of_numbers)

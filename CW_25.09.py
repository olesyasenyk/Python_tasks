# import pyowm

# owm = pyowm.OWM('a2c2f94427b1b4dd2407f7654738bfe6')  
# city=input('What city are you interested in? ')
# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_place(city)
# w = observation.get_weather()
# temperature=w.get_temperature('celsius')['temp']
# humidity=w.get_humidity()
# wind=w.get_wind() ['speed']
# print("In " + city + " city" + " the temperature of the air is" + " " + str(temperature) + " Celsius.")
# print("The humidity of the air is" + " " + str(humidity) + '.')
# print("The wind is" + " " + str(wind) + " meters per second.")
# print("In this city we have "+ w.get_detailed_status()+'.')

#                             # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>

# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)

# from random import randint
# x=randint(1,100)
# print(x)
# guess=int(input('I have a number in my mind. It\'s between 1 and 100. Guess, what is it? '))
# while True:
#     if x>guess:
#         print ('You\'re wrong, it\'s bigger than that.')
#         guess=int(input('Let\'s make another guess: '))
#     elif x<guess:
#         print ('You\'re wrong, it\'s smaller than that.')
#         guess=int(input('Let\'s make another guess: '))
#     elif x==guess:
#         print ('Congratulations! You won!')
#         answer=(input('Let\'s play one more time? Type yes or no: '))
#         if answer.lower()=='yes':
#             guess=int(input('I have a number in my mind. It\'s between 1 and 100. Guess, what is it? '))
#         elif answer.lower()=='no':
#             print ('Thanks for playing. See you!')
#             break
#         else:
#             print ('Error. Restart the game.')
#             break
#     else:
#         print ('The number you typed is beyond the given range.')
#         guess=int(input('Let\'s make another guess: '))

# # що робити, якщо юзер вводить неправильний тип даних
# # все спочатку після еррор

# from math import pow
# from math import pi 
# rect_side_1=int(input('Give one side of the rectangle: '))
# rect_side_2=int(input('Give the other side of the rectangle: '))
# print('The area of the rectangle is {}.'.format(rect_side_1*rect_side_2))
# tri_side=int(input('Give the side of the triangle: '))
# tri_base=int(input('Give the base of the triangle: '))
# print('The area of the triangle is {}.'.format(tri_side*tri_base*0.5))
# radius=int(input('Give the radius of the circle: '))
# print('The area of the circle is {}.'.format(pi*pow(radius,2)))
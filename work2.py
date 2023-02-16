print('Ex. 1')
a = 'Hi, my friend, I want to go to the park'
print(a)
b = 'Hi, my friend, I want to go to the cinema'
a = b
print(a)

print('Ex. 2')
user_name = input('Write your name:')
print('Hi, my friend,' + user_name + ', I want to go to the cinema')

#цитата відомої людини
print('Ex. 3')
famous_person = 'Bo Bennett '
message = '"Success is not in what you have, but who you are."'
print(famous_person + 'once said,' + message)

print('Ex. 4')
my_name="  \t Oksana\n   "
a=my_name.lstrip()
b=my_name.rstrip()
c=my_name.strip()
print(a)
print(b)
print(c)

print('Ex. 5')
print('\n Oksana Zhetariuk \n Ukraine \n 58012 \n Cherniwtsi \n Vorobkevycha \n 31b')

print('Ex. 6')
meters = input('Number:')
inch_in_meters = 0.03
foot_in_meters = 0.3
mile_in_meters = 1609
yard_in_meters = 0,9144

a = meters * inch_in_meters
b = meters * foot_in_meters
c = meters * mile_in_meters
d = meters * yard_in_meters

print (a)
print (b)
print (c)
print (d)

#завдання показує скільки канікули привали у секунда хвилинах та годинах
print('Ex. 7')
days_in_holiday = 3
seconds = 60
minutes = seconds * 60

seconds_in_holiday = days_in_holiday * 60 * 60 * 24
minutes_in_holiday = days_in_holiday * minutes
hours_in_holiday = days_in_holiday * 24
print(seconds_in_holiday)
print(minutes_in_holiday)
print(hours_in_holiday)

print('Ex. 8')
c = input('Number:')
f = 32 + 9/5 * c
k = c + 273,15
print(f)
print(k)

#дистанція між Пекіном та Києвом
print('Ex. 10')
import math
x1 = 39.9075000
x2 = 116.3972300
y1 = 50.4546600
y2 = 30.5238000
a1= math.radians(x1)
a2= math.radians(x2)
b1= math.radians(y1)
b2= math.radians(y2)

distancee = 6371.032 * math.acos(math.sin(a1) * math.sin(a2) + math.cos(a1) * math.cos(a2) * math.cos(b1 - b2))
print(distancee) 

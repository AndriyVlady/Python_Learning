print("Hello, Python!") 

euros_count = 100

# BEGIN (write your solution here)
dollars_count = euros_count * 1.25 
uan_count = dollars_count * 6.91
print(str(dollars_count) + "\n" + str(uan_count))

print(dollars_count)
print(uan_count)
# END


info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."

first_name = "Joffrey"
greeting = "Hello"

# BEGIN (write your solution here)
print(greeting + ", " + first_name + "! " + intro + "\n" + info)
# END


king = "Rooms in King Balon's Castles:"

# BEGIN (write your solution here)
new_rooms = 6
kings_ammount = 17
print (king, new_rooms * kings_ammount)
# END


value = 1.34567
print (value)
print (str(value))
value = int(value)
print (value)
print (float(value))

float_num = 1.234556767
int_num = 5
print (float_num + int_num)
print (str(float_num) + str(int_num))

first_name = 'Alexander'
first_name =  ('B' + first_name[1:])
print(first_name)  

company1 = "Apple"
company2 = "Samsung"

# BEGIN (write your solution here)
print (pow(len(company1), len(company2)))
# END


text = "Never forget what you are, for surely the world will not"

# BEGIN (write your solution here)
length_text = len(text)
print (f'First: {text[length_text - length_text]} Last: {text[length_text - 1]}')
# END

from random import random 
#print (int(round(random(),1) * 10))
print (round(random() * 10))


row = '1,4,6,8,10,12,14,16,18,20'.split(',')

print (max(row))
print (max(1,4,6,8,10,12,14,16,18,20))
int_num  = -5
print (int_num.__abs__())
print (abs.__doc__)

first_name = "  Grigor     5676"

# BEGIN (write your solution here)
print (first_name.strip('. !'))
# END


text = "Never forget what you are, for surely the world will not"

# BEGIN (write your solution here)
print (f'Index Of N: {text.find('N')}\nIndex Of ,: {text.find(',')}')
# END

name = 'Tirion'
print(name.replace('Ti', 'Ki').lower())

name = 'Tirion'
# Чему равен результат такого вызова?
print(name[1:5].upper().find('I'))


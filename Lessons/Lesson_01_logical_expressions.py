# Lesson 01: Logical Expressions
def number_check(num):
    if num == 0:
        return "\"Это НОЛЬ.\""
    elif num % 2 ==0:
        return "\"Число четное.\""
    else:
        return "\"Число нечетное.\""
age = input("Введите число: ")

try:
    print("Вы ввели значение:", age)
    age = int(age)
    print ("Ваше число:", age, "-", number_check(age))
except ValueError:
    print("Ошибка: Введите корректное целое число.")
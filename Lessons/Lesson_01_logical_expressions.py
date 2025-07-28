age = int(input("Введите число: "))
print("Вы ввели число:", age)

def number_check(num):
    if num == 0:
        return "\"Это НОЛЬ.\""
    elif num % 2 ==0:
        return "\"Число четное.\""
    else:
        return "\"Число нечетное.\""

print ("Ваше число:", age, "-", number_check(age))

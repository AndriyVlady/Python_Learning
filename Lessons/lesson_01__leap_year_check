def is_leap_year(year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        return True
    return False

year = input ("Введите год: ")
try:
    print ("Вы ввели значение: ", year)
    year = int(year)
    if year == 0:
        print ("Вы ввели НОЛЬ.")
    elif is_leap_year(year):
        print ("Вы ввели високосный год:", year)
    else:
        print ("Вы ввели обычный год:", year)
except ValueError:
    print ("Ошибка: Введите корректное целое года.")
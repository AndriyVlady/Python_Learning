from lesson_01_break import __break__

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        return True
    return False

def run_is_leap_year():  
    
    while True:
        year = input ("Введите год: ")
        try:
            print ("Вы ввели значение: ", year)
            year = int(year)
            if year == 0:
                print ("Вы ввели НОЛЬ.")
                __break__()
            elif year < 0:
                print ("Вы ввели високосный год:", year)
                __break__()
            else:
                print ("Вы ввели обычный год:", year)
                __break__()
        except ValueError:
            print ("Ошибка: Введите корректное целое года.")

if __name__ == "__main__":
    run_is_leap_year()
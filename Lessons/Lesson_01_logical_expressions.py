# Lesson 01: Logical Expressions

from lesson_01_break import __break__

def number_check(num):
    if num == 0:
        return "\"Это НОЛЬ.\""
    elif num % 2 ==0:
        return "\"Число четное.\""
    else:
        return "\"Число нечетное.\""
def run_logical_expressions():
    while True:
        age = input("Введите число: ")
        try:
            print("Вы ввели значение:", age)
            age = int(age)
            print ("Ваше число:", age, "-", number_check(age))
            __break__()
        except ValueError:
            print("Ошибка: Введите корректное целое число.")

if __name__ == "__main__":
    run_logical_expressions()
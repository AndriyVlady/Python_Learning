from lesson_01__leap_year_check import run_is_leap_year
from Lesson_01_logical_expressions import run_logical_expressions
from lesson_01_break import __break__



def main_menu():
    print("Добро пожаловать в программу проверки!")
    while True:
        print("Выберите действие:")
        print ("Какую проверку вы хотите выполнить? \n 1 - Проверка на високосный год \n 2 - Проверка чётности числа \n 3 - Выход из программы")
        choice = input("Введите свой выбор (1/2/3): ")

        if choice == '1':
            run_is_leap_year()
            __break__()
        elif choice == '2':
            run_logical_expressions()
            __break__()
        elif choice == '3':
            __break__()
            
        else:
            print("Ошибка: введите 1, 2 или 3. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
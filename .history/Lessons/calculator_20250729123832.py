import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        op = operation.get()

        if op == "Сложение":
            result = a + b
        elif op == "Вычитание":
            result = a - b
        elif op == "Умножение":
            result = a * b
        elif op == "Деление":
            if b == 0:
                messagebox.showerror("Ошибка", "Деление на ноль невозможно")
                return
            result = a / b
        else:
            result = "Выберите операцию"

        label_result.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

root = tk.Tk()
root.title("Простой калькулятор")

tk.Label(root, text="Число 1").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Число 2").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

operation = tk.StringVar(value="Сложение")
ops = ["Сложение", "Вычитание", "Умножение", "Деление"]

tk.OptionMenu(root, operation, *ops).grid(row=2, column=0, columnspan=2)

tk.Button(root, text="Вычислить", command=calculate).grid(row=3, column=0, columnspan=2)

label_result = tk.Label(root, text="Результат: ")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()

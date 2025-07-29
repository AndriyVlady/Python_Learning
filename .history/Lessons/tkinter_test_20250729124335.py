import tkinter as tk

root = tk.Tk()           # Создаем главное окно
root.title("Привет, Tkinter!")  # Заголовок окна

label = tk.Label(root, text="Привет, мир!")  # Создаем метку с текстом
label.pack()             # Размещаем метку в окне

root.mainloop()          # Запускаем цикл обработки событий

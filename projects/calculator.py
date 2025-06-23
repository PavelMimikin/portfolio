import tkinter as tk
from tkinter import font

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

def button_click(char):
    entry.insert(tk.END, char)

def clear():
    entry.delete(0, tk.END)

# Создаем главное окно
root = tk.Tk()
root.title("Красивый калькулятор")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

# Настраиваем шрифт
custom_font = font.Font(size=14)

# Поле ввода
entry = tk.Entry(root, width=14, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Кнопки
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Создаем и размещаем кнопки
row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=10, font=custom_font,
                 bg="#4CAF50", fg="white", command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button, padx=20, pady=10, font=custom_font,
                 bg="#e0e0e0", command=lambda b=button: button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Кнопка очистки
tk.Button(root, text="C", padx=20, pady=10, font=custom_font,
         bg="#f44336", fg="white", command=clear).grid(row=row, column=col, columnspan=4, sticky="we", padx=5, pady=5)

# Запускаем главный цикл
root.mainloop()

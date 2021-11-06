from tkinter import *
import tkinter as tk

from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import numpy as np

root = Tk()

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 300
h = h - 225
root.geometry('600x300+{}+{}'.format(w, h))
root.title("Метод дерева рішень")

showinfo(
        title='Оберіть файл з матрицею',
        message='Будь ласка, оберіть файл з матрицею!'
    )

filetypes = (
    ('text files', '*.txt'),
    ('All files', '*.*')
)

filename = fd.askopenfilename(
    title='Відкрити файл',
    initialdir='/',
    filetypes=filetypes)

class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=10, font=('Arial', 10))
                self.e.grid(row=i, column=j, padx=10, pady=10)
                self.e.insert(END, lst[i][j])

lst = np.loadtxt(filename, dtype='f', delimiter=',')

total_rows = len(lst)
total_columns = len(lst[0])
t = Table(root)

def count():

    lst = np.loadtxt(filename, dtype='f', delimiter=',')

    # Розрахунок очікуваних доходів при будівництві великого заводу
    big_factory = (lst[0][1] * lst[0][2] + lst[0][3] * lst[0][4]) * 5 - lst[0][0]

    # Розрахунок очікуваних доходів при будівництві малого заводу
    small_factory = (lst[1][1] * lst[1][2] + lst[1][3] * lst[1][4]) * 5 - lst[1][0]

    # Розрахунок очікуваних доходів при будівництві заводів при отриманні позитивної інформації
    pos_info_big_factory = (lst[0][1] * lst[2][2] + lst[0][3] * lst[2][3]) * 4 - lst[0][0]
    pos_info_small_factory = (lst[1][1] * lst[2][2] + lst[1][3] * lst[2][3]) * 4 - lst[1][0]
    pos_info = (pos_info_big_factory + pos_info_small_factory) * 0.8

    # Розрахунок очікуваних доходів при будівництві заводів при отриманні негативної інформації
    neg_info = 0 * lst[2][1]

    # Визначення варіанту рішення з найбільшим доходом
    high_income = {big_factory: 'А', small_factory: 'Б', pos_info: 'В', neg_info: 'В'}
    high_income = high_income.get(max(high_income))

    text1.delete("1.0", END)
    text1.insert("1.0", high_income)
    text1.insert("1.0", '\n Варіант рішення з найбільшим доходом: ')
    text1.insert("1.0", ' , оскільки заводи не будують!\n')
    text1.insert("1.0", ' тис. $')
    text1.insert("1.0", neg_info)
    text1.insert("1.0", '\n   Очікуваний дохід від заводів при негативній інформації: \n   ')
    text1.insert("1.0", 'тис. $')
    text1.insert("1.0", pos_info)
    text1.insert("1.0", '\nВ) Очікуваний дохід від заводів при позитивній інформації: ')
    text1.insert("1.0", ' тис. $')
    text1.insert("1.0", small_factory)
    text1.insert("1.0", '\nБ) Очікуваний дохід при будівництві малого заводу: ')
    text1.insert("1.0", ' тис. $')
    text1.insert("1.0", big_factory)
    text1.insert("1.0", 'А) Очікуваний дохід при будівництві великого заводу: ')

labelframe = LabelFrame(root, text="Розв'язок", width=580, height=175)
labelframe.place(x=10, y=120)

text1 = tk.Text(width=70, height=9)
text1.place(x=15, y=140)

b1 = tk.Button(text="Обчислити", command=count).place(x=500, y=47)

root.mainloop()

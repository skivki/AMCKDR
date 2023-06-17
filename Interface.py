# Импортируем библиотеку tkinter и присваиваем ей псевдоним tk
import tkinter as tk
# Импортируем все классы из модуля tkinter
from tkinter import *
# Импортируем класс ImageTk и Image из библиотеки PIL
from PIL import ImageTk,Image
# Импортируем подмодуль pyplot из библиотеки matplotlib и присваиваем ему псевдоним plt
import matplotlib.pyplot as plt
# Импортируем класс Combobox из подмодуля ttk модуля tkinter и присваиваем ему псевдоним Combobox
from tkinter.ttk import Combobox

# Импортируем класс Font из модуля tkinter.font
import pandas as pd
# Импортируем класс Font из модуля tkinter.font
from tkinter.font import Font

# Читаем файл Excel  с помощью функции read_excel из библиотеки pandas и присваиваем его переменной file
file1 = pd.read_excel('AAPL.xlsx')
file2 = pd.read_excel('AMZN.xlsx')
file3 = pd.read_excel('BABA.xlsx')
file4 = pd.read_excel('CVX.xlsx')
file5 = pd.read_excel('MSFT.xlsx')
file6 = pd.read_excel('NKE.xlsx')
file7 = pd.read_excel('NVDA.xlsx')
file8 = pd.read_excel('INTC.xlsx')
file9 = pd.read_excel('TM.xlsx')
file10 = pd.read_excel('SEB.xlsx')
file11 = pd.read_excel('WMT.xlsx')
#основное окно ws
ws = Tk()
# Устанавливаем заголовок основного окна
ws.title("Анализ акций компаний")
# Устанавливаем начальный размер основного окна
ws.state('zoomed')
# Создаем объект класса Canvas с размером 1920x1920 и присваиваем его переменной canvas,
# который будет служить прямоугольной областью для рисования
canvas = tk.Canvas(ws,width=1920,height=1080 )#это прямоугольная область
canvas.pack()
# Создаем объект класса Label с текстом 'Добро пожаловать', шрифтом Arial Bold и размером 100,
# и присваиваем его переменной lbl
lbl = Label(ws, text='Добро пожаловать', font=("Arial Blod", 100))
lbl.place(x=240, y=180)
# Открываем изображение 'AM1.png' с помощью класса Image из библиотеки PIL и присваиваем его переменной image
image = Image.open("AM1.png")
# Создаем объект класса PhotoImage из переменной image с помощью класса ImageTk из библиотеки PIL и присваиваем его переменной photo
photo = ImageTk.PhotoImage(image)
# Создаем изображение на canvas из переменной photo с координатами x=200, y=80 и присваиваем его переменной image
image = canvas.create_image(200, 80,image=photo)
# Создаем переменную n типа StringVar() и присваиваем ей пустое значение
n = tk.StringVar()
values=['NVIDIA','Microsoft','Apple','Walmart','Chevron','Toyota','Seabord','Intel','Alibaba','Nike']
# Создаем объект класса Combobox со значениями values и присваиваем его переменной combo
combo = Combobox(ws,width=35,height=8,font=("Arial bold", 14),values = values, textvariable = n )
# Создаем объект класса Font со шрифтом Arial и размером 14 и присваиваем его переменной font
font = Font(family = "Arial", size = 14)
# Устанавливаем шрифт font для списка значений Combobox
ws.option_add("*TCombobox*Listbox*Font", font)

# Создаем функцию nw(), которая выполнится при нажатии на кнопку Начать анализ
def nw():
    lbl1 = Label(ws, text='Выберите компанию', font=("Arial bold", 80))
    # Удаляем кнопку Начать анализ с основного окна ws
    button.place_forget()
    lbl2 = Label(ws, text='Если вы не смогли найти интересующий вас "элемент",то проверте текст на ошибки', font=("Arial bold", 15))
    # Удаляем lbl с основного окна ws
    lbl.place_forget()
    # Выбираем текущий элемент в Combobox
    combo.current()
    # это всё геометрическое расположение на окне
    combo.place(x=560, y=330)
    lbl1.place(x=250, y=150)
    lbl2.place(x=100, y=600)
    # Привязка события "ComboboxSelected" к функции callback
    combo.bind("<<ComboboxSelected>>",  callback)
    # Создание кнопки "очистить" и размещение ее на главном окне ws с заданными параметрами
    button2 = Button(ws, text='очистить', command=clear_combobox,font=("Arial Blod", 12))
    button2.place(x=980, y=328)
# Создание кнопки "Начать анализ" с заданными параметрами и размещение ее на главном окне ws
button = tk.Button(ws, text="Начать анализ", bg='Violet', fg='Blue', font=("Arial Blod", 20),command=nw)
button.place(x=650, y=460)

# Определение значений для оси X и Y в переменных x1...x11 и y соответственно
x1 = file1['Date'].tolist()
y1 = file1['Close'].tolist()
x2 = file2['Date'].tolist()
y2 = file2['Close'].tolist()
x3 = file3['Date'].tolist()
y3 = file3['Close'].tolist()
x4 = file4['Date'].tolist()
y4 = file4['Close'].tolist()
x5 = file5['Date'].tolist()
y5 = file5['Close'].tolist()
x6 = file6['Date'].tolist()
y6 = file6['Close'].tolist()
x7 = file7['Date'].tolist()
y7 = file7['Close'].tolist()
x8 = file8['Date'].tolist()
y8 = file8['Close'].tolist()
x9 = file9['Date'].tolist()
y9 = file9['Close'].tolist()
x10 = file10['Date'].tolist()
y10 = file10['Close'].tolist()
x11 = file11['Date'].tolist()
y11 = file11['Close'].tolist()
# если строяться справа на лево, то переворачиваем данные столбцов
x1.reverse()
x2.reverse()
x3.reverse()
x4.reverse()
x5.reverse()
x6.reverse()
x7.reverse()
x8.reverse()
x9.reverse()
x10.reverse()
x11.reverse()
y1.reverse()
y2.reverse()
y3.reverse()
y4.reverse()
y5.reverse()
y6.reverse()
y7.reverse()
y8.reverse()
y9.reverse()
y10.reverse()
y11.reverse()

# Описание функции callback, которая будет вызываться при выборе значения в combobox
def callback(eventObject):
    # Если выбрано значение "Apple" в combobox, то выполняется следующее:
    if combo.get() == "Apple":
        # Строится график по точкам с координатами, определенными в переменных x1 и y1
        plt.plot(x1,y1,color='black')
        plt.bar(x1, y1 )
    elif combo.get() == "Amazon":
        plt.plot(x2,y2,color='black')
        plt.bar(x2, y2 )
    elif combo.get() == "Alibaba":
        plt.plot(x3, y3,color='black')
        plt.bar(x3, y3)
    elif combo.get() == "Chevron":
        plt.plot(x4, y4,color='black')
        plt.bar(x4, y4 )
    elif combo.get() == "Microsoft":
        plt.plot(x5, y5,color='black')
        plt.bar(x5, y5 )
    elif combo.get() == "Nike":
        plt.plot(x6, y6,color='black')
        plt.bar(x6, y6 )
    elif combo.get() == "NVIDIA":
        plt.plot(x7, y7,color='black')
        plt.bar(x7, y7)
    elif combo.get() == "Intel":
        plt.plot(x8, y8,color='black')
        plt.bar(x8, y8 )
    elif combo.get() == "Toyota":
        plt.plot(x9, y9,color='black')
        plt.bar(x9, y9 )
    elif combo.get() == "Seabord":
        plt.plot(x10, y10,color='black')
        plt.bar(x10, y10 )
    elif combo.get() == "Walmart":
        plt.plot(x11, y11,color='black')
        plt.bar(x11, y11 )

    # Установка названия для оси Y
    plt.ylabel('цена акции в USD')
    # Установка названия для оси X
    plt.xlabel('период времени')  # для подписей осей
    # Получение текущей оси графика
    ax = plt.subplot()
    # Установка шага на оси x
    ax.xaxis.set_major_locator(plt.MultipleLocator(300))
    # Отображение графика
    plt.show()

# Описание функции clear_combobox, которая будет вызываться при нажатии на кнопку "очистить
def clear_combobox():
    combo.set("")# устанавливаем пустое значение в комбобокс

ws.mainloop()




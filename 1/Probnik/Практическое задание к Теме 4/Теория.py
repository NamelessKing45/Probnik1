'''
from math import* #Добавление библиотеки math
print(math.sqrt(4)) #math.sqrt корень из числа
'''

import tkinter
my_window=tkinter.Tk()


my_window.title('мое первое приложение')
my_lable=tkinter.Label(text='тестовый текст')
my_lable2=tkinter.Label(text='тестовый текст 2',font = 10)

my_canva=tkinter.Canvas(my_window,width=500,height=500,background='red')
my_canva.create_line(0,250,250,250,width=10,fill='blue')
my_canva.create_oval(50,50,100,100,width=10,fill='blue')
my_canva.create_line(300,300,300,250,width=10,fill='blue')
my_canva.create_line(0,500,200,500,width=10,fill='blue')
my_canva.create_oval(100,500,100,500,width=10,fill='blue')
'''координаты по X, координаты по Y, ширина, цвет'''


my_lable.pack()
my_lable2.pack()
my_canva.pack()
my_window.mainloop()
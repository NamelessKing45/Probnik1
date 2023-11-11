from tkinter import *  # добавление библиотеки

a1 = Tk()
a1.title('Программа')
b1 = Canvas(a1, width=1000, height=1000, bg='white', cursor="arrow")
c1 = Label(text="Программа", font=80)
b1.create_text(300, 100, text='Условие задачи:', font="Arial 30", fill="black")
b1.create_text(200, 250, text='Скорость первого бегуна = 4 ', font="Arial 20", fill="black")
b1.create_text(200, 350, text='Скорость второго бегуна = 9', font="Arial 20", fill="black")
b1.create_text(200, 450, text='Дистанция = 400', font="Arial 20", fill="black")
b1.create_text(200, 800, text='Точка пересечения 123 км', font="Arial 20", fill="black")
b1.create_line(0, 900, 1000, 900, width=10, fill="black", dash=(10, 2))
b1.create_line(10, 900, 990, 900, width=10, fill="red", dash=(10, 2))

b1.create_oval(210, 890, 230, 910, width=5, fill="red")
b1.create_text(150, 930, text='Первый бегун пробежал 183 км.', font="Arial 10", fill="black")
b1.create_text(550, 930, text='Второй бегун пробежал 277 км.', font="Arial 10", fill="black")
c1.pack()
b1.pack()

a1.mainloop()

# #print("1")
# #input("x=".)
# #print("hi-hi")
# #print("by-by")
#
#
# #name = input("как тебя зовут? ")
# #age = int(input("сколь вам лет "))
# #num_school = input("В какой школе ты учишься? ")
# #hobbies = input("Какое у тебя хобби? ")
# #city = input("В каком городе ты жившь? ")
# #point = input("Где встретимся? ")
#
# #print("Привет", name,", рад знакомству, тебе в следующем году будет", age + 1,". Я тоже учусь в школе №", num_school, "и живу в городе", city,". Давай займёмся", hobbies, ". Может быть вместе встретимся в", point, ".")
#
#
# str1 = ("Я.внима?тельноне_слушал учителя.и?не_понял.всё!!!")
# a = str1.replace("_"," ").replace(".", " ").replace("?","").replace("!!!","!").replace("!!!","!").replace("ине","и не")
# print(a)
#
#Импорт
from tkinter import*
runner1=2
runner2=2
distance=1200
time=distance/runner1+runner2
distance1=time*runner1
distance2=time*runner2

#настройка окон
new_window = Tk()
canvas = Canvas(new_window, width=1000, height=1000, bg="white", cursor="arrow")
new_window.title('Программа')
my_title = Label(text='Програма', font=40)




#создание объектов
canvas.create_text(500, 100, text=f'Условие задачи:', font="Arial 24", anchor='n', justify=LEFT, fill="black")
canvas.create_line(0,500,1000,500,width=5,fill='black')
canvas.create_oval(800, 800, 1000, 1000, width=5, fill='black')



#отрисовка
my_title.pack()
canvas.pack()
new_window.mainloop()

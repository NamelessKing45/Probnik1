import tkinter
window=tkinter.Tk()
canvas=tkinter.Canvas(window,height=1000,width=1000,background='white', cursor = 'boat')
window.title('Проект')
my_label1=tkinter.Label(text='Конкурс', font= "Times_New_Roman 50"  ,)
my_label1.pack()
canvas.create_line(500,0,500,1000,width=5,fill='red')
canvas.pack()
window.mainloop()
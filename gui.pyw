import tkinter as tk
from tkinter import ttk
from tkinter import IntVar
from tkinter import StringVar
import sys
import time
from time import sleep
import datetime
import winsound
now = datetime.datetime.now()



class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('245x160')  # размер
        self.attributes('-alpha', 1)  # прозрачность
        #self.attributes('-topmost', True)  # поверх всех окон
        # self.overrideredirect(True)
        self.resizable(False, False)  # не разрешать изменять размер
        self.title('Напоминалка')  # титл
        self.iconbitmap(r'icon//Task Scheduler.ico')

        self.set_ui()  # запуск set_ui

    def set_ui(self):

        global hour1
        hour1 = IntVar()

        #self.time2 = ttk.LabelFrame(self)
        #self.time2.pack(fill=tk.X)
        #self.time2 = ttk.Label(self,text='Ниже введите нужно вам время',padding=(10,10,10,00))
        #self.time2.pack()
        self.hour = ttk.LabelFrame(self,padding=(10,0,10,10))
        self.hour.pack(fill=tk.X)
        self.time3 = ttk.Label(self.hour,text='Время:',padding=(-2,10,10,10))
        self.time3.pack(side=tk.LEFT)
        self.hour1 = ttk.Entry(self.hour, width=4, textvariable=hour1)
        self.hour1.pack(side=tk.LEFT)
        self.time4 = ttk.Label(self.hour,text=' : ',padding=(0,0,0,0))
        self.time4.pack(side=tk.LEFT)

        global minute1
        minute1 = IntVar()
        #self.minute = ttk.LabelFrame(self,padding=(10,10,10,10))
        #self.minute.pack(fill=tk.X)
        self.minute1 = ttk.Entry(self.hour, width=4,textvariable=minute1)
        self.minute1.pack(side=tk.LEFT)

        global comment1
        comment1 = StringVar()
        self.comment = ttk.LabelFrame(self, text='Напоминание: ',padding=(5,10,10,0))
        self.comment.pack(fill=tk.X)
        self.comment1 = ttk.Entry(self.comment, width=40,textvariable=comment1)
        self.comment1.pack(side=tk.LEFT)

        self.buttons = ttk.LabelFrame(self)
        self.buttons.pack(fill=tk.X)
        cont_but = ttk.Button(self.buttons, text="Продолжить",command=self.app_cont,padding=(0,0,0,0)).pack(side=tk.LEFT)
        stop_music = ttk.Button(self.buttons, text="Стоп", command=self.stop_music,padding=(0,0,0,0)).pack(side=tk.LEFT)  # кнопка
        exit_but = ttk.Button(self.buttons, text="Выход", command=self.app_exit,padding=(15,0,0,0)).pack(side=tk.LEFT)
        

    def app_cont(self):
        while True:
            now = datetime.datetime.now()
            if now.hour > hour1.get() or now.minute > minute1.get():
                return True
            else:
                if now.hour == hour1.get() and now.minute == minute1.get():
                    winsound.PlaySound('sound//Timer.wav',winsound.SND_ASYNC | winsound.SND_LOOP)
                    return True

    
    def stop_music(Self):
         winsound.PlaySound('sound//Silent.wav',winsound.SND_PURGE | winsound.SND_ASYNC)

    def app_exit(self):  # команда для работы кнопки "Выход"
        self.destroy()
        sys.exit()


root = Application()

root.mainloop()
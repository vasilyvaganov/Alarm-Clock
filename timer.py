import time
import datetime
import winsound
import sys
now = datetime.datetime.now()
period = []
info = []
shot = 0


def enter():
    while True:
        global info
        global shot
        global hour
        global minute
        global wait_time
        global comment
        try:
            hour = int(input("Введите кол-во часов: "))
            minute = int(input("Введите кол-во минут: "))
            wait_time = (hour*60+minute)-(now.hour*60+now.minute)
            comment = str(input("Введите название напоминания: "))
            times = datetime.time(hour, minute)
            period.append(str(times))
        except ValueError:
            shot = 1
            break
        print(period)
        stop = input('Если все то напишите да, если нет, то нажмите <enter>: ')
        # Защита от пустой строки или  символов
        if stop == None:
            enter()
        elif stop == 'да':
            shot = 0
            break
        print(period)
    return period


clack = enter()
while shot == 1:
    enter()

while True:
    now = datetime.datetime.now()
    if now.hour > hour or now.minute > minute:
        break
    else:
        if now.hour == hour and now.minute == minute:
            print(" Время окончено.", '\n', 'Ваш комментарий:', comment)
            winsound.PlaySound('Timer.wav', winsound.SND_ASYNC)
            break
    time.sleep(1)

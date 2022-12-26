import time
from tkinter import *
import winsound
import pywhatkit

try:
    ph = int(input('Enter the phone number : '))
    msg = input('Enter the message : ')
except ValueError:
    print('Please give valid input')

phone = '+91' + f'{ph}'


def countdown(t):
    root = Tk()
    root.geometry("400x250")
    root.title("Timer")
    root.iconbitmap(r'Timer.ico')
    root['bg']='black'
    hour = StringVar()
    minute = StringVar()
    second = StringVar()
    h, m, s = map(int, t.split(":"))
    hr = int(time.strftime("%H"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    hour.set(h-hr)
    minute.set((m-mn+1))
    second.set((s-sec-50))
    txt = Label(root, text='Your message will be delivered in...', font=('Calibri', 18), bg='black', fg='white')
    txt.place(x=30, y=10)
    hourEntry = Entry(root, width=3, font=('Calibri', 18), textvariable=hour)
    hourEntry.place(x=80, y=60)
    des = Label(root, text='H', font=('Calibri', 15), bg='black', fg='white')
    des.place(x=80, y=100)
    colon = Label(root, text=':', font=('Calibri', 18, 'bold'), bg='black', fg='white')
    colon.place(x=125, y=60)
    minuteEntry = Entry(root, width=3, font=('Calibri', 18), textvariable=minute)
    minuteEntry.place(x=140, y=60)
    des = Label(root, text='M', font=('Calibri', 15), bg='black', fg='white')
    des.place(x=140, y=100)
    colon = Label(root, text=':', font=('Calibri', 18, 'bold'), bg='black', fg='white')
    colon.place(x=185, y=60)
    secondEntry = Entry(root, width=3, font=('Calibri', 18), textvariable=second)
    secondEntry.place(x=200, y=60)
    des = Label(root, text='S', font=('Calibri', 15), bg='black', fg='white')
    des.place(x=200, y=100)
    def submit():
        try:
            temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        except:
            print("Please input the right value")
        while temp > -1:
            mins, secs = divmod(temp, 60)
            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
            root.update()
            time.sleep(1)
            temp -= 1
        if(int(hour.get())==0 and int(minute.get())==0 and int(second.get())==0):
            root.destroy()
            winsound.Beep(4500,300)
            pywhatkit.sendwhatmsg(phone, msg, h, m+1)
    submit()
    root.mainloop()
countdown(input("Enter time in (HH:MM:SS) format : "))

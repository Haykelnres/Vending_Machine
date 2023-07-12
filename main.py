from tkinter import *
from tkinter import messagebox
import time
from pygame import mixer
root = Tk()
root.title("Автомат горячих напитков")
s = 0
t, ti, ident = False, True, False
sum = 0
c = Canvas(root, width=500, height=650)
mixer.init()
soundWater = mixer.Sound('water.mp3')
soundClick = mixer.Sound('click.mp3')
soundFinish = [mixer.Sound('launch1.mp3'), mixer.Sound('twinkle_far1.mp3')]

avtomat_body = c.create_rectangle(314, 440, 200, 800, outline='burlywood4', fill='CadetBlue4', tag="group2")
avtomat_okno = c.create_rectangle(220, 570, 240, 540, outline='gray31', fill='gray31', tag="group2")
avtomat_sliv = c.create_rectangle(226, 548, 235, 540, outline='gray', fill='gray', tag="group2")
avtomat_ekran = c.create_rectangle(265, 470, 300, 480, outline='dark slate gray', fill='gray52', tag="group2")
avtomat_knopki = c.create_rectangle(263, 500, 302, 550, outline='gray11', fill='LightYellow4', tag="group2")
avtomat_sdacha = c.create_rectangle(296, 580, 270, 590, outline='gray11', fill='gray24', tag="group2")
head = c.create_oval(500, 500, 450, 450, outline='sienna2', fill='sienna2', tag="group1")
body = c.create_rectangle(490, 600, 460, 500, outline='green', fill='green', tag="group1")
legs = c.create_rectangle(485, 600, 464, 4900, outline='grey', fill='grey', tag="group1")

c.pack()
class human:
    def move_left(self):
        soundStep = mixer.Sound('sand1.mp3')
        for i in range(31):
            if i % 10 == 0:
                soundStep.play()
            c.move('group1', -5, 0)    # движение человека к автомату
            c.update()
            time.sleep(0.05)
human.move_left(1)
time.sleep(1)

avtomat_body_full = c.create_rectangle(0, 0, 501, 651, outline='burlywood4', fill='CadetBlue4', tag="group3")

koshel = c.create_rectangle(0, 560, 220, 800, fill="brown4")
money1 = c.create_oval(110, 595, 135, 620, fill="azure")
money2 = c.create_oval(110, 625, 135, 650, fill="azure")
money5 = c.create_oval(140, 595, 165, 620, fill="azure")
money10 = c.create_oval(140, 625, 165, 650, fill="azure")
c.create_text(123, 606, anchor='c', fill='black', font='Times 10', text='1р')
c.create_text(123, 636, anchor='c', fill='black', font='Times 10', text='2р')
c.create_text(153, 606, anchor='c', fill='black', font='Times 10', text='5р')
c.create_text(153, 636, anchor='c', fill='black', font='Times 10', text='10р')
money50 = c.create_rectangle(0, 565, 100, 614, fill="green")
money100 = c.create_rectangle(0, 590, 100, 670, fill="green")
money500 = c.create_rectangle(0, 620, 100, 660, fill="green")
karta = c.create_rectangle(175, 580, 210, 700, fill = 'chocolate3')
c.create_text(190, 619, anchor='c', fill='black', font='Times 10', text='Скидочная\nкарта',angle = 90)
c.create_text(85, 572, anchor='c', fill='khaki', font='Times 10', text='50р')
c.create_text(85, 600, anchor='c', fill='khaki', font='Times 10', text='100р')
c.create_text(85, 630, anchor='c', fill='khaki', font='Times 10', text='500р')
avtomat_okno_full = c.create_rectangle(80, 410, 190, 550, outline='black', fill='gray31', tag="group3")
avtomat_sliv_full = c.create_rectangle(119, 410, 153, 430, outline='gray', fill='gray', tag="group3")
avtomat_sdacha_full = c.create_rectangle(380, 490, 465, 560, outline='gray11', fill='gray24', tag="group3")
kupyry = c.create_rectangle(388, 170, 465, 190, outline='gray11', fill='gray24', tag="group4")  #
kupyry2 = c.create_rectangle(400, 180, 454, 180, outline='black', fill='black', tag="group4")
monety = c.create_rectangle(423, 198, 429, 220, fill='gray20')
monety2 = c.create_rectangle(425, 200, 427, 218, fill='black')
karder = c.create_rectangle(320, 170, 360, 210, outline='black', fill='gray35', tag="group3")
karder2 = c.create_oval(330, 180, 350, 200, fill='gray63')
c.create_text(138, 50, anchor='c', fill='yellow3', font='Times 28', text='Горячие\nнапитки')
vozvrat = c.create_rectangle(390, 400, 460, 420, fill='grey')
c.create_text(425, 410, anchor='c', fill='orange', font='Times 10', text='Возврат')


def Drink(event):
    global sum, ti, ident
    ident = True
    soundDrink = mixer.Sound('drink.mp3')
    soundDrink.play()
    c.delete('Pol2')
    c.delete('PolMain')
    c.update()
    time.sleep(0.5)
    soundDrink.play()
    time.sleep(0.5)
    refund(event)

def Question():
    answer = messagebox.askyesno(message="Желаете продолжить?")
    if not answer and sum == 0:
        c.delete("all")
        c.update()
        c.create_rectangle(314, 440, 200, 800, outline='burlywood4', fill='CadetBlue4', tag="group2")
        c.create_rectangle(220, 570, 240, 540, outline='gray31', fill='gray31', tag="group2")
        c.create_rectangle(226, 548, 235, 540, outline='gray', fill='gray', tag="group2")
        c.create_rectangle(265, 470, 300, 480, outline='dark slate gray', fill='gray52', tag="group2")
        c.create_rectangle(263, 500, 302, 550, outline='gray11', fill='LightYellow4', tag="group2")
        c.create_rectangle(296, 580, 270, 590, outline='gray11', fill='gray24', tag="group2")
        c.create_oval(350, 500, 300, 450, outline='sienna2', fill='sienna2', tag="group1")
        c.create_rectangle(340, 600, 310, 500, outline='green', fill='green', tag="group1")
        c.create_rectangle(335, 600, 314, 4900, outline='grey', fill='grey', tag="group1")

        c.pack()

        class human:
            def move_left(self):
                soundStep = mixer.Sound('sand1.mp3')
                for i in range(41):
                    if i % 10 == 0:
                        soundStep.play()
                    c.move('group1', 5, 0)  # движение человека к автомату
                    c.update()
                    time.sleep(0.05)

        human.move_left(1)
        soundFinish[0].play()
        time.sleep(1.5)
        soundFinish[1].play()
        time.sleep(2)
        exit()

def Create_Coffee():
    global sum, soundWater, t
    if t:
        N = 31
    else:
        N = 35
    if sum >= N:
        sum -= N
        points = [95, 490, 115, 550, 155, 550, 175, 490]
        c.create_polygon(points, outline='red', fill='white', width=2, tag="PolMain")
        c.update()
        time.sleep(1)
        c.create_rectangle(125, 430, 148, 490, fill="brown", tag="Rec1")
        c.update()
        soundWater.play()
        for i in range(20, 1, -1):
            c1 = 63.24555 / i
            h = 60 / i
            x1 = 115 - ((c1 ** 2 - h ** 2)**0.5)
            x2 = 155 + ((c1 ** 2 - h ** 2)**0.5)
            c.create_polygon(x1, 550-h, 115, 550, 155, 550, x2, 550-h, fill="brown", tag="Rec")
            c.update()
            time.sleep(0.05)
            c.delete("Rec")
        c.create_polygon(104.16667, 517.5, 115, 550, 155, 550, 165.83333, 517.5, fill="brown", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.create_polygon(103.33334, 515, 115, 550, 155, 550, 166.66666, 515, fill="brown", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.create_polygon(102.50001, 512.5, 115, 550, 155, 550, 167.49999, 512.5, fill="brown", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.delete("Rec")
        c.delete("Pol1")
        c.create_polygon(102.76668, 510, 115.5, 549.4, 154.45, 549.4, 167.43332, 510, fill="brown", tag="Pol2")
        c.tag_bind("Pol2", '<Button-1>', Drink)
        c.update()
        c.delete("Rec1")
        c.update()
        w.config(text=f"Баланс равен {sum}₽")
    else:
        w.config(text="Внесено недостаточно денег.")
def Create_Tea():
    global sum, soundWater, t
    if t:
        N = 36
    else:
        N = 40
    if sum >= N:
        sum -= N
        points = [95, 490, 115, 550, 155, 550, 175, 490]
        c.create_polygon(points, outline='red', fill='white', width=2, tag="PolMain")
        c.update()
        time.sleep(1)
        c.create_rectangle(125, 430, 148, 490, fill="saddle brown", tag="Rec1")
        c.update()
        soundWater.play()
        for i in range(20, 1, -1):
            c1 = 63.24555 / i
            h = 60 / i
            x1 = 115 - ((c1 ** 2 - h ** 2)**0.5)
            x2 = 155 + ((c1 ** 2 - h ** 2)**0.5)
            c.create_polygon(x1, 550-h, 115, 550, 155, 550, x2, 550-h, fill="saddle brown", tag="Rec")
            c.update()
            time.sleep(0.05)
            c.delete("Rec")
        c.create_polygon(104.16667, 517.5, 115, 550, 155, 550, 165.83333, 517.5, fill="saddle brown", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.create_polygon(103.33334, 515, 115, 550, 155, 550, 166.66666, 515, fill="saddle brown", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.create_polygon(102.50001, 512.5, 115, 550, 155, 550, 167.49999, 512.5, fill="saddle brown", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.delete("Rec")
        c.delete("Pol1")
        c.create_polygon(102.76668, 510, 115.5, 549.4, 154.45, 549.4, 167.43332, 510, fill="saddle brown", tag="Pol2")
        c.tag_bind("Pol2", '<Button-1>', Drink)
        c.update()
        c.delete("Rec1")
        c.update()
        w.config(text=f"Баланс равен {sum}₽")
    else:
        w.config(text="Внесено недостаточно денег.")
def Create_Cocoa():
    global sum, soundWater, t
    if t:
        N = 27
    else:
        N = 30
    if sum >= N:
        sum -= N
        points = [95, 490, 115, 550, 155, 550, 175, 490]
        c.create_polygon(points, outline='red', fill='white', width=2, tag="PolMain")
        c.update()
        time.sleep(1)
        c.create_rectangle(125, 430, 148, 490, fill="brown3", tag="Rec1")
        c.update()
        soundWater.play()
        for i in range(20, 1, -1):
            c1 = 63.24555 / i
            h = 60 / i
            x1 = 115 - ((c1 ** 2 - h ** 2) ** 0.5)
            x2 = 155 + ((c1 ** 2 - h ** 2) ** 0.5)
            c.create_polygon(x1, 550 - h, 115, 550, 155, 550, x2, 550 - h, fill="brown3", tag="Rec")
            c.update()
            time.sleep(0.05)
            c.delete("Rec")
        c.create_polygon(104.16667, 517.5, 115, 550, 155, 550, 165.83333, 517.5, fill="brown3", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.create_polygon(103.33334, 515, 115, 550, 155, 550, 166.66666, 515, fill="brown3", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.create_polygon(102.50001, 512.5, 115, 550, 155, 550, 167.49999, 512.5, fill="brown3", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.delete("Rec")
        c.delete("Pol1")
        c.create_polygon(102.76668, 510, 115.5, 549.4, 154.45, 549.4, 167.43332, 510, fill="brown3", tag="Pol2")
        c.tag_bind("Pol2", '<Button-1>', Drink)
        c.update()
        c.delete("Rec1")
        c.update()
        w.config(text=f"Баланс равен {sum}₽")
    else:
        w.config(text="Внесено недостаточно денег.")
def Create_Jelly():
    global sum, soundWater, t
    if t:
        N = 22
    else:
        N = 25
    if sum >= N:
        sum -= N
        points = [95, 490, 115, 550, 155, 550, 175, 490]
        c.create_polygon(points, outline='red', fill='white', width=2, tag="PolMain")
        c.update()
        time.sleep(1)
        c.create_rectangle(125, 430, 148, 490, fill="pink", tag="Rec1")
        c.update()
        soundWater.play()
        for i in range(20, 1, -1):
            c1 = 63.24555 / i
            h = 60 / i
            x1 = 115 - ((c1 ** 2 - h ** 2) ** 0.5)
            x2 = 155 + ((c1 ** 2 - h ** 2) ** 0.5)
            c.create_polygon(x1, 550 - h, 115, 550, 155, 550, x2, 550 - h, fill="pink", tag="Rec")
            c.update()
            time.sleep(0.05)
            c.delete("Rec")
        c.create_polygon(104.16667, 517.5, 115, 550, 155, 550, 165.83333, 517.5, fill="pink", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.create_polygon(103.33334, 515, 115, 550, 155, 550, 166.66666, 515, fill="pink", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.create_polygon(102.50001, 512.5, 115, 550, 155, 550, 167.49999, 512.5, fill="pink", tag="Rec")
        c.update()
        time.sleep(0.05)
        c.delete("Rec")
        c.delete("Pol1")
        c.create_polygon(102.76668, 510, 115.5, 549.4, 154.45, 549.4, 167.43332, 510, fill="pink", tag="Pol2")
        c.tag_bind("Pol2", '<Button-1>', Drink)
        c.update()
        c.delete("Rec1")
        c.update()
        w.config(text=f"Баланс равен {sum}₽")
    else:
        w.config(text="Внесено недостаточно денег.")


button1 = Button(root, text="кофе\n35₽", height=2, width=5, command=Create_Coffee)
button2 = Button(root, text="чай\n40₽", height=2, width=5, command=Create_Tea)
button3 = Button(root, text="какао\n30₽", height=2, width=5, command=Create_Cocoa)
button4 = Button(root, text="кисель\n25₽", height=2, width=5, command=Create_Jelly)

cbut1 = c.create_window(400, 300, window=button1)           #кнопки
cbut2 = c.create_window(450, 300, window=button2)
cbut3 = c.create_window(400, 346, window=button3)
cbut4 = c.create_window(450, 346, window=button4)
w = Label(root, width=25, text="Добрый день,внесите сумму.", fg="green2", bg="gray52")    #текстовое поле
w1 = c.create_window(400, 100, window=w)
def summ1(event):
    global sum, soundClick
    soundClick.play()
    sum = sum + 1
    w.config(text=f'внесен {sum}₽')
def summ2(event):
    global sum, soundClick
    soundClick.play()
    sum = sum + 2
    w.config(text=f'внесено {sum}₽')
def summ5(event):
    global sum, soundClick
    soundClick.play()
    sum = sum + 5
    w.config(text=f'внесено {sum}₽')
def summ10(event):
    global sum, soundClick
    soundClick.play()
    sum = sum + 10
    w.config(text=f'внесено {sum}₽')
def summ50(event):
    global sum, soundClick
    soundClick.play()
    sum = sum + 50
    w.config(text=f'внесено {sum}₽')
def summ100(event):
    global sum, soundClick
    soundClick.play()
    sum = sum + 100
    w.config(text=f'внесено {sum}₽')
def summ500(event):
    global sum, soundClick
    soundClick.play()
    sum = sum + 500
    w.config(text=f'внесено {sum}₽')
c.tag_bind(money1, '<Button-1>', summ1)
c.tag_bind(money2, '<Button-1>', summ2)
c.tag_bind(money5, '<Button-1>', summ5)
c.tag_bind(money10, '<Button-1>', summ10)
c.tag_bind(money50, '<Button-1>', summ50)
c.tag_bind(money100, '<Button-1>', summ100)
c.tag_bind(money500, '<Button-1>', summ500)
def refund(event):
    global sum, ident
    if sum > 0:
        sum = 0
        w.config(text='Заберите сдачу')
        c.create_rectangle(385, 520, 460, 560, fill='green', tag="sdacha")
        c.tag_bind("sdacha", '<Button-1>', delete)
    elif ident:
        ident = False
        Question()
c.tag_bind(vozvrat, '<Button-1>', refund)
def delete(event):
    global ti, ident
    c.delete("sdacha")
    c.update()
    ti = False
    if ident:
        Question()
    w.config(text='Добрый день,внесите сумму.')
def skidka(event):
    global soundClick, t
    t = True
    soundClick.play()
    w.config(text='Ваша скидка - 10%')
    button1.config(text="кофе\n31₽")
    button2.config(text="чай\n36₽")
    button3.config(text="какао\n27₽")
    button4.config(text="кисель\n22₽")
c.tag_bind(karta, '<Button-1>', skidka)
c.focus_set()
root.mainloop()
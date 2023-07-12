from tkinter import *
import time
import math

root = Tk()

c = Canvas(root, width=500, height=650)
root.geometry('500x650')
x, y = 0, 0


def Create_Glass(event):
    points = [100, 50, 120, 110, 160, 110, 180, 50]
    c.create_polygon(points, outline='red', fill='white', width=2, tag="PolMain")
    c.update()
    time.sleep(1)
    c.create_rectangle(130, 0, 150, 50, fill="deep sky blue", tag="Rec1")
    c.update()
    time.sleep(0.6)
    c.create_polygon(113.33334, 90, 120, 110, 160, 110, 166.66666, 90, fill="deep sky blue", tag="Pol1")
    c.update()
    time.sleep(0.6)
    c.delete("Pol1")
    c.create_polygon(107.76668, 70, 120.5, 109.4, 159.45, 109.4, 172.43332, 70, fill="deep sky blue", tag="Pol2")
    c.update()
    c.delete("Rec1")
    c.update()


def Drink(event):
    global x, y
    c.create_polygon(430, 500, 430, 590, 470, 590, 470, 500, outline="grey80", fill="green", tag="group3")
    c.update()
    time.sleep(1)
    for i in range(46):
        c.delete("group3")
        x += 0.1
        y += 0.1
        if i > 35:
            c.create_polygon(430, 500,
                             430+math.cos(x)*150, 590+math.sin(y)*150,
                             470+math.cos(x)*150, 590+math.sin(y)*150,
                             470+math.cos(x)*3, 500+math.sin(y)*3, outline="grey80", fill="green", tag="group3")
            c.update()
            time.sleep(0.05)
    # while x != 1:
    #     c.delete("PolMain")
    #     x += 0.1
    #     y += 0.1
    #     points = [100+math.cos(x)*10, 50+math.sin(y)*10,
    #               120+math.cos(x)*80, 110+math.sin(y)*80,
    #               160+math.cos(x)*80, 110+math.sin(y)*80,
    #               180+math.cos(x)*80, 50+math.sin(y)*80]
    #     c.create_polygon(points, outline='red', fill='white', width=2, tag="PolMain")
    #     c.update()
    #     time.sleep(0.05)


head = c.create_oval(500, 500, 400, 400, outline='sienna2', fill='sienna2', tag="group1")
body = c.create_rectangle(490, 600, 410, 500, outline='green', fill='green', tag="group1")
# arms = c.create_rectangle(470, 590, 430, 500, outline='grey', fill='green', tag="group3")
# wrist = c.create_rectangle(470, 590, 430, 570, outline='sienna2', fill='sienna2', tag="group3")
legs = c.create_rectangle(475, 600, 425, 650, outline='grey', fill='grey', tag="group1")


c.pack()
BtnWater = Button(root, text="Налить воды", command=Create_Glass)
# BtnWater.place(x=200, y=500)
BtnWater.pack()
BtnDrink = Button(root, text="Выпить воды", command=Drink)
# BtnDrink.place(x=300, y=500)
BtnDrink.pack()
c.focus_set()
root.mainloop()
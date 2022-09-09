#coding:utf-8

import tkinter as kinder
import pygame
import threading
import random

from pygame.constants import QUIT
from pygame.display import flip, set_caption


pygame.init()
res=[640,480]
randomColor = [random.randrange(255),random.randrange(255),random.randrange(255)]
randomValue = [random.randrange(600),random.randrange(400)]
surface=pygame.display.set_mode(res)
set_caption("Geometry!")

def tk():
    app=kinder.Tk()
    app.geometry("320x180+0+0")
    app.title("Commandes")
    circleButton=kinder.Button(app,text="Circle", command=DrawCircle)
    circleButton.pack()
    rectButton=kinder.Button(app,text="Rectangle", command=DrawRectangle)
    rectButton.pack()
    lineButton=kinder.Button(app,text="Line", command=DrawLine)
    lineButton.pack()
    eraseButton=kinder.Button(app,text="Erase", command=Erase)
    eraseButton.pack()
    app.mainloop()


def DrawCircle():
    pygame.draw.circle(surface,randomColor , randomValue, random.randrange(100))
    flip()

def DrawRectangle():
    pygame.draw.rect(surface, randomColor , pygame.Rect(random.randrange(100),random.randrange(200),random.randrange(600),random.randrange(400)),width=3)
    flip()

def DrawLine():
    pygame.draw.line(surface, randomColor , randomValue, randomValue)
    flip()

def Erase():
    surface.fill([0,0,0])
    flip()

threading.Thread(target=tk).start()

launched=True

while launched:
    for event in pygame.event.get():
        if event.type==QUIT:
            launched=False

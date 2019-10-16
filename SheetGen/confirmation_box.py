from tkinter import *
from tkinter.ttk import *
import pygame as pyg
import sheet_draw as sd
import media as m
import time
import sys

def confirmation_box():
    root = Tk()
    root.title('Sheet Hero')
    root.iconbitmap(m.ico)

    root.A = Frame(root)
    root.A.pack(side = TOP, pady = 10)

    root.B = Frame(root)
    root.B.pack(side = LEFT, padx = 20)

    root.C = Frame(root)
    root.C.pack(side = RIGHT, padx = 20)

    root.D = Frame(root)
    root.D.pack(side = BOTTOM, pady = 10)

    root.geometry('450x140+475+250')

    def yes():

        sd.generate_pdf()
        progress = Progressbar(root.D, orient = HORIZONTAL, length = 100, mode = 'determinate')
        progress.pack()
        progress['value']=5
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=10
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=15
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=20
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=25
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=30
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=35
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=40
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=45
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=50
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=55
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=60
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=65
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=70
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=75
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=80
        root.update_idletasks()
        time.sleep(0.25)
        progress['value']=85
        root.update_idletasks()
        time.sleep(0.2)
        progress['value']=90
        root.update_idletasks()
        time.sleep(0.04)
        progress['value']=95
        root.update_idletasks()
        time.sleep(0.1)
        progress['value']=100

        quit()


    def no():
        raise SystemExit()

    root.msg = Label(root.A, text = 'Você quer salvar a partitura?')
    #msg['font']  = ('Calibri', '10')
    root.msg.pack()

    root.button = Button(root.C, command = yes)
    root.button['text']  = '✓ Sim'
    #root.button['font']  = ('Calibri', '10')
    root.button['width'] = 20
    root.button.pack()

    root.button = Button(root.B, command = no)
    root.button['text']  = '✗ Não'
    #root.button['font']  = ('Calibri', '10')
    root.button['width'] = 20
    root.button.pack()

    root.mainloop()

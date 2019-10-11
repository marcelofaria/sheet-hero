from tkinter import *
import pygame as pyg
import sheet_draw as sd
import media as m

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

    root.geometry('400x100+475+250')

    def yes():
        sd.generate_pdf()
        #pyg.quit()
        exit()

    def no():
        #pyg.quit()
        exit()

    root.msg = Label(root.A)
    root.msg['text']  = 'Voce quer salvar a partitura?'
    root.msg['font']  = ('Calibri', '10')
    root.msg.pack()


    root.button = Button(root.C, command = yes)
    root.button['text']  = 'Sim'
    root.button['font']  = ('Calibri', '10')
    root.button['width'] = 20
    root.button.pack()

    root.button = Button(root.B, command = no)
    root.button['text']  = 'Não'
    root.button['font']  = ('Calibri', '10')
    root.button['width'] = 20
    root.button.pack()

    root.mainloop()

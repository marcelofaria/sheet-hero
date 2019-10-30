from tkinter import *
import spectrum as sp
import media as m

root = Tk()
root.title('Sheet Hero')
root.iconbitmap(m.ico)

root.A = Frame(root)
root.A.pack(side = TOP)

root.B = Frame(root)
root.B.pack(side = LEFT, anchor = N)

root.D = Frame(root)
root.D.pack(side = RIGHT, anchor = N)

root.C = Frame(root)
root.C.pack(anchor = N)

root.E = Frame(root)
root.E.pack(side = BOTTOM)

root.geometry('400x490+475+100')

def get_values():
    compass = v.get()
    clef    = b.get()
    tempo   = c.get()
    title   = root.txt_field.get()

    #results = str(compass) + ' ' + str(clef) + ' ' + str(tempo)
    #print(title)
    root.ok['command'] = root.destroy
    root.ok.invoke()
    sp.sheet_hero(compass, clef, tempo, title)

v = IntVar()
b = IntVar()
c = IntVar()

root.msg = Label(root.A, text = 'Bem vindo! Configure sua partitura')
root.msg['font'] = ('Calibri', '10', 'bold')
root.msg.pack()

root.msg = Label(root.A, text = 'Digite o Título')
root.msg['font'] = ('Calibri', '10')
root.msg.pack()

root.txt_field = Entry(root.A, width = 60, justify = CENTER)
root.txt_field.pack()

root.msg = Label(root.A, text = 'Escolha o Andamento')
root.msg['font'] = ('Calibri', '10')
root.msg.pack()

root.radio = Radiobutton(root.A, text = '60 bpm', value = 24, variable = c)
root.radio.pack()
root.radio = Radiobutton(root.A, text = '75 bpm', value = 25, variable = c)
root.radio.pack()
root.radio = Radiobutton(root.A, text = '90 bpm', value = 26, variable = c)
root.radio.pack()

root.msg = Label(root.A, text = 'Escolha a Armadura de Compasso')
root.msg['font'] = ('Calibri', '10')
root.msg.pack()

root.radio = Radiobutton(root.A, text = '4/4', value = 1, variable = v)
root.radio.pack()
root.radio = Radiobutton(root.A, text = '6/8', value = 2, variable = v)
root.radio.pack()

root.msg = Label(root.A, text = 'Escolha a Armadura de Clave')
root.msg['font'] = ('Calibri', '10')
root.msg.pack()

root.radio = Radiobutton(root.B, text = 'Dó Maior', value = 3, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Ré Maior', value = 4, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Mi Maior', value = 5, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Fá Maior', value = 6, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Sol Maior', value = 7, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Lá Maior', value = 8, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Si Maior', value = 9, variable = b, state = DISABLED)
root.radio.pack()

root.radio = Radiobutton(root.C, text = 'Dó# Maior', value = 10, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Ré# Maior', value = 11, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Mi# Maior', value = 12, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Fá# Maior', value = 13, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Sol# Maior', value = 14, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Lá# Maior', value = 15, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Si# Maior', value = 16, variable = b, state = DISABLED)
root.radio.pack()

root.radio = Radiobutton(root.D, text = 'Dób Maior', value = 17, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Réb Maior', value = 18, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Mib Maior', value = 19, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Fáb Maior', value = 20, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Solb Maior', value = 21, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Láb Maior', value = 22, variable = b, state = DISABLED)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Sib Maior', value = 23, variable = b, state = DISABLED)
root.radio.pack()

root.msg = Label(root.E, text = ' ')
root.msg['font'] = ('Calibri', '10')
root.msg.pack()


root.ok = Button(root.E, command=get_values)
root.ok['text'] = 'Confirmar'
root.ok['font'] = ('Calibri', '10')
root.ok['width'] = 50
#root.ok['command'] = root.destroy
root.ok.pack()

root.msg = Label(root.E, text = ' ')
root.msg['font'] = ('Calibri', '10')
root.msg.pack()

root.mainloop()


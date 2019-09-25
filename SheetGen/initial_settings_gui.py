from tkinter import *
import spectrum

root = Tk()
root.title('Sheet Hero')
root.iconbitmap('C:\\Users\\MarceloAugustoStefan\\Desktop\\TCC\\sheet-gen\\SheetGen\\media\\colcheia_Vew_icon.ico')

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

root.geometry('400x350+475+100')

def get_values():
    compass = v.get()
    clef    = b.get()

    results = str(compass) + ' ' + str(clef)
    print(results)
    root.ok['command'] = root.destroy
    root.ok.invoke()
    spectrum.sheet_hero(compass, clef)

root.msg = Label(root.A, text = 'Bem vindo ao SheetHero')
root.msg['font'] = ('Calibri', '10', 'bold')
root.msg.pack()

root.msg = Label(root.A, text = 'Configure sua partitura')
root.msg['font'] = ('Calibri', '10')
root.msg.pack()

root.msg = Label(root.A, text = 'Escolha a Armadura de Compasso')
root.msg['font'] = ('Calibri', '10')
root.msg.pack()

v = IntVar()
b = IntVar()

root.radio1 = Radiobutton(root.A, text = '4/4', value = 1, variable = v)
root.radio1.pack()
root.radio2 = Radiobutton(root.A, text = '6/8', value = 2, variable = v)
root.radio2.pack()

root.msg = Label(root.A, text = 'Escolha a Armadura de Clave')
root.msg['font'] = ('Calibri', '10')
root.msg.pack()

root.radio = Radiobutton(root.B, text = 'Dó Maior', value = 3, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Ré Maior', value = 4, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Mi Maior', value = 5, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Fá Maior', value = 6, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Sol Maior', value = 7, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Lá Maior', value = 8, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.B, text = 'Si Maior', value = 9, variable = b)
root.radio.pack()

root.radio = Radiobutton(root.C, text = 'Dó# Maior', value = 10, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Ré# Maior', value = 11, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Mi# Maior', value = 12, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Fá# Maior', value = 13, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Sol# Maior', value = 14, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Lá# Maior', value = 15, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.C, text = 'Si# Maior', value = 16, variable = b)
root.radio.pack()

root.radio = Radiobutton(root.D, text = 'Dób Maior', value = 17, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Réb Maior', value = 18, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Mib Maior', value = 19, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Fáb Maior', value = 20, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Solb Maior', value = 21, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Láb Maior', value = 22, variable = b)
root.radio.pack()
root.radio = Radiobutton(root.D, text = 'Sib Maior', value = 23, variable = b)
root.radio.pack()

root.ok = Button(root.E, command=get_values)
root.ok['text'] = 'Confirmar'
root.ok['font'] = ('Calibri', '10')
root.ok['width'] = 50
#root.ok['command'] = root.destroy
root.ok.pack()

root.mainloop()




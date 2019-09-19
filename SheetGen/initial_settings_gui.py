from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text = 'Bem vindo ao SheetHero')
        self.msg['font'] = ('Calibri', '10', 'italic', 'bold')
        self.msg.pack()
        self.msg1 = Label(self.widget1, text = 'Configure sua partitura')
        self.msg1['font'] = ('Calibri', '10')
        self.msg1.pack()
        self.sair = Button(self.widget1)
        self.sair['text'] = 'Sair'
        self.sair['font'] = ('Calibri', '10')
        self.sair['width'] = 5
        self.sair['command'] = self.widget1.quit
        self.sair.pack()

root = Tk()
Application(root)
root.mainloop()

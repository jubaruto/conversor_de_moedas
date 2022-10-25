from cgitb import text
from email.mime import image
from tkinter import *

tela = Tk()
tela.title('Conversor de Moedas')
tela.geometry('300x450+500+150')
tela.resizable(False, False)
tela.config(bg='#32CD32')


logo = PhotoImage(file='C:\Projetos\conversor_de_moedas\img\imagem1.png')
logo = logo.subsample(3, 3)
img1 = Label(image=logo, bg='#32CD32')

lixeira = PhotoImage(file='C:\Projetos\conversor_de_moedas\img\lixeira.png')
lixeira = lixeira.subsample(25, 20)
img2 = Label(image=lixeira, bg='#32CD32')


framedolar = Frame(tela, borderwidth=1.5, relief='solid',  bg='#32CD32')
labeldolar = Label(tela, text='Dolar', bg='#32CD32')
textodolar = Entry(framedolar, width=45,)


framereal = Frame(tela, borderwidth=1.5, relief='solid',  bg='#32CD32')
labelreal = Label(tela, text='Real', bg='#32CD32')
textoreal = Entry(framereal, width=45,)

bconversao = Button(tela, text='Conversão', font=('Georgia', 15),
                    highlightthickness=0, bd=0, bg='#32CD32', borderwidth=1.5, relief='solid',)
                    
blixo = Button(tela, image=lixeira, highlightthickness=0, bd=0, bg='#32CD32')


img1.place(x=70, y=10)

framedolar.place(x=5, y=183, width=285, height=48)
labeldolar.place(x=10, y=185)
textodolar.place(x=5, y=20)

framereal.place(x=5, y=258, width=285, height=48)
labelreal.place(x=10, y=260)
textoreal.place(x=5, y=20)

bconversao.place(x=90, y=350)
blixo.place(x=270, y=320)




tela.mainloop()



from tkinter import *

tela = Tk()
tela.title('Conversor de Moedas')
tela.geometry('500x500+400+150')
tela.resizable(False, False)

logo = PhotoImage(file='C:\Projetos\conversor_de_moedas\img\images.png')
logo = logo.subsample(1,1)
img1 = Label(image=logo)

img1.place(x=100, y=50)

tela.mainloop()
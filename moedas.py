from cgitb import text
from email.mime import image
from tkinter import *
from click import command
from tkinter import messagebox
from numpy import real
from requests import *

url = get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
url_format = url.json()

dolarhj = url_format['USDBRL']['bid']
dolarhj = float(dolarhj)
dolarhj = round(dolarhj, 2)

eurohj = url_format['EURBRL']['bid']
eurohj = float(eurohj)
eurohj = round(eurohj, 2)

tela = Tk()
tela.title('Conversor de Moedas')
tela.geometry('300x600+500+50')
tela.resizable(False, False)
tela.config(bg='#32CD32')

def conversao():
    try:
        if textoreal.get() == '' and textoeuro.get() == '':
            dolar = float(textodolar.get())
            
            real = dolar * dolarhj
            textoreal.insert(0, round(real, 2))         
            
            euro = real / eurohj
            textoeuro.insert(0, round(euro, 2))
            
        elif textodolar.get() == '' and textoeuro.get() == '':
            real = float(textoreal.get())
            
            dolar = real / dolarhj
            textodolar.insert(0, round(dolar, 2))       
            
            euro = real / eurohj
            textoeuro.insert(0, round(euro, 2))
            
        elif textoreal.get() == '' and textodolar.get() == '':
            euro = float(textoeuro.get())
            
            real = euro * eurohj
            textoreal.insert(0, round(real, 2))         
            
            dolar = real / dolarhj
            textodolar.insert(0, round(dolar, 2))
            
    except ValueError:
        messagebox.showerror('Atenção!!', 'Insira um valor!')

def limpar():
    textodolar.delete(0, END)
    textoreal.delete(0, END)
    textoeuro.delete(0, END)

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

frameeuro = Frame(tela, borderwidth=1.5, relief='solid',  bg='#32CD32')
labeleuro = Label(tela, text='Euro', bg='#32CD32')
textoeuro = Entry(frameeuro, width=45,)

frameyen = Frame(tela, borderwidth=1.5, relief='solid',  bg='#32CD32')
labelyen = Label(tela, text='Iene', bg='#32CD32')
textoyen = Entry(frameyen, width=45,)


bconversao = Button(tela, text='Conversão', font=('Georgia', 15),
                    highlightthickness=0, bd=0, bg='#32CD32', borderwidth=1.5, relief='solid', command=conversao)
                    
blixo = Button(tela, image=lixeira, highlightthickness=0, bd=0, bg='#32CD32', command=limpar)


img1.place(x=70, y=10)

framedolar.place(x=5, y=183, width=285, height=48)
labeldolar.place(x=10, y=185)
textodolar.place(x=5, y=20)

framereal.place(x=5, y=258, width=285, height=48)
labelreal.place(x=10, y=260)
textoreal.place(x=5, y=20)

frameeuro.place(x=5, y=333, width=285, height=48)
labeleuro.place(x=10, y=335)
textoeuro.place(x=5, y=20)

frameyen.place(x=5, y=408, width=285, height=48)
labelyen.place(x=10, y=410)
textoyen.place(x=5, y=20)

bconversao.place(x=90, y=500)
blixo.place(x=270, y=460)




tela.mainloop()



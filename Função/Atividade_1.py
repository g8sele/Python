from tkinter import *
from tkinter import messagebox

teste_botao01():
    print("Você clicou no botão")


def msg_aviso():
    messagebox.showwarning("Aviso - Está é uma mensagem de aviso")


def msg_info():
    messagebox.showinfo("Informação - Está é uma mensagem de informação")


menu_inicial = Tk()

menu_inicial.title("Exemplo Mensagem")
menu_inicial.geometry("500x500")

rotulo1 = Label(menu_inicial, text="Tipos de Mensagens")
bg = "blue", fg = "white", font = "Arial 24 bold"

botao01 = Button(menu_inicial, text="Clique aqui!")
(command=teste_botao01)

botao02 = Button(menu_inicial, text="Mensagem de Aviso")
(command=msg_aviso)

botao03 = Button(menu_inicial, text="Mensagem de Informação")
(command=msg_info)


rotulo1.grid(row=0, column=0)
botao01.grid(row=1, column=0, sticky=W)
botao02.grid(row=2, column=0, sticky=W)
botao03.grid(row=3, column=0, sticky=W)

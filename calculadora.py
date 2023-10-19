import customtkinter as ctk
from tkinter import *
from tkinter import messagebox


# Funcoes de calcular, limpar tela e clicar botao
def clickar_botao(numero):
    display.insert(END, numero)


def limpar_tudo():
    display.delete(0,END)


def calcular():
    try:
        calculo = display.get()
        novo_calculo = calculo.replace('X','*')
        resultado = eval(novo_calculo)
        limpar_tudo()
        display.insert(0,resultado)

    # Aqui vamos tratar possiveis erros
    except ZeroDivisionError:
        messagebox.showerror('Erro', 'Não é possível dividir por 0')
    except:
        messagebox.showerror('Erro', 'Entre valores válidos')


# Criando a janela
janela = ctk.CTk()
janela.title('Calculadora')
janela.geometry('300x300')
janela.config(bg='#36373B')

fonte = ('Arial', 20, 'bold')


# Criando o display da calculadora

display = ctk.CTkEntry(janela, font=fonte, text_color='#000000', border_color='#fff', fg_color='#fff', width=280, height=50)
display.place(x=10,y=10)

# Criando botões

btn1 = ctk.CTkButton(janela, command=lambda: clickar_botao('7'), font=fonte, text_color='#000000', text='7', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn1.place(x=10,y=80)


btn2 = ctk.CTkButton(janela, command=lambda: clickar_botao('8'), font=fonte, text_color='#000000', text='8', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn2.place(x=80,y=80)


btn3 = ctk.CTkButton(janela, command=lambda: clickar_botao('9'), font=fonte, text_color='#000000', text='9', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn3.place(x=150,y=80)


btn4 = ctk.CTkButton(janela, command=lambda: clickar_botao('4'), font=fonte, text_color='#000000', text='4', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn4.place(x=10,y=125)


btn5 = ctk.CTkButton(janela, command=lambda: clickar_botao('5'), font=fonte, text_color='#000000', text='5', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn5.place(x=80,y=125)


btn6 = ctk.CTkButton(janela, command=lambda: clickar_botao('6'), font=fonte, text_color='#000000', text='6', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn6.place(x=150,y=125)


btn7 = ctk.CTkButton(janela, command=lambda: clickar_botao('1'), font=fonte, text_color='#000000', text='1', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn7.place(x=10,y=170)


btn8 = ctk.CTkButton(janela, command=lambda: clickar_botao('2'), font=fonte, text_color='#000000', text='2', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn8.place(x=80,y=170)


btn9 = ctk.CTkButton(janela, command=lambda: clickar_botao('3'), font=fonte, text_color='#000000', text='3', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn9.place(x=150,y=170)


btn10 = ctk.CTkButton(janela, command=lambda: clickar_botao('0'), font=fonte, text_color='#000000', text='0', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn10.place(x=10,y=215)


btn11 = ctk.CTkButton(janela, command=lambda: clickar_botao('.'), font=fonte, text_color='#000000', text='.', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn11.place(x=80,y=215)


btn12 = ctk.CTkButton(janela, command=limpar_tudo, font=fonte, text_color='#000000',  text='C', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn12.place(x=150,y=215)


btn13 = ctk.CTkButton(janela, command=calcular, font=fonte, text='=', hover_color='#7DF305', border_width=2, cursor='hand2', width=60)
btn13.place(x=10,y=255)


btn14 = ctk.CTkButton(janela, command=lambda: clickar_botao('+'), font=fonte, text='+', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn14.place(x=220,y=80)


btn15 = ctk.CTkButton(janela, command=lambda: clickar_botao('-'), font=fonte, text='-', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn15.place(x=220,y=125)


btn16 = ctk.CTkButton(janela, command=lambda: clickar_botao('X'), font=fonte, text='X', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn16.place(x=220,y=170)


btn17 = ctk.CTkButton(janela, command=lambda: clickar_botao('/'), font=fonte, text='/', hover_color='#FFFFFF', border_width=2, cursor='hand2', width=60)
btn17.place(x=220,y=215)

janela.mainloop()


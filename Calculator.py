from tkinter import *

def inserir_valor(valor):
    ety.delete(0,"end")
    ety.insert(0,valor)
    pass

def adicao():
    global operacao_atual
    operacao_atual = "+"
    global valor_atual
    valor_atual = int(ety.get())
    pass

def subtracao():
    global operacao_atual
    operacao_atual = "-"
    global valor_atual
    valor_atual = int(ety.get())
    pass

def multiplicacao():
    global operacao_atual
    operacao_atual = "*"
    global valor_atual
    valor_atual = int(ety.get())
    pass

def divisao():
    global operacao_atual
    operacao_atual = "/"
    global valor_atual
    valor_atual = int(ety.get())
    pass

def limpar():
    ety.delete(0, "end")
    global operacao_atual
    operacao_atual = ""
    global valor_atual
    valor_atual = 0
    pass

def resultado():
    global valor_atual
    global operacao_atual

    if operacao_atual == "+":
        novo_valor = ety.get()
        ety.delete(0, "end")
        ety.insert(0, valor_atual + int(novo_valor))
    if operacao_atual == "-":
        novo_valor = ety.get()
        ety.delete(0, "end")
        ety.insert(0, valor_atual - int(novo_valor))
    if operacao_atual == "*":
        novo_valor = ety.get()
        ety.delete(0, "end")
        ety.insert(0, valor_atual * int(novo_valor))
    if operacao_atual == "/":
        novo_valor = ety.get()
        ety.delete(0, "end")
        ety.insert(0, valor_atual / int(novo_valor))
    pass


janela = Tk()
janela.geometry("500x500+100+100")
janela.title("Calculator")

ety = Entry(janela)
ety.grid(row=0, column=0, columnspan=4, ipadx=50, ipady=10, padx=5, pady=5)

btn1 = Button(janela, text="1", command= lambda: inserir_valor("1"))
btn2 = Button(janela, text="2", command= lambda: inserir_valor("2"))
btn3 = Button(janela, text="3", command= lambda: inserir_valor("3"))
btn4 = Button(janela, text="4", command= lambda: inserir_valor("4"))
btn5 = Button(janela, text="5", command= lambda: inserir_valor("5"))
btn6 = Button(janela, text="6", command= lambda: inserir_valor("6"))
btn7 = Button(janela, text="7", command= lambda: inserir_valor("7"))
btn8 = Button(janela, text="8", command= lambda: inserir_valor("8"))
btn9 = Button(janela, text="9", command= lambda: inserir_valor("9"))
btn0 = Button(janela, text="0", command= lambda: inserir_valor("0"))

btn1.grid(row=1, column=0, ipadx=20, ipady=10)
btn2.grid(row=1, column=1, ipadx=20, ipady=10)
btn3.grid(row=1, column=2, ipadx=20, ipady=10)
btn4.grid(row=2, column=0, ipadx=20, ipady=10)
btn5.grid(row=2, column=1, ipadx=20, ipady=10)
btn6.grid(row=2, column=2, ipadx=20, ipady=10)
btn7.grid(row=3, column=0, ipadx=20, ipady=10)
btn8.grid(row=3, column=1, ipadx=20, ipady=10)
btn9.grid(row=3, column=2, ipadx=20, ipady=10)
btn0.grid(row=4, column=0, ipadx=20, ipady=10)

btnAdicao = Button(janela, text="+", command= lambda: adicao())
btnSubtracao = Button(janela, text="-", command= lambda: subtracao())
btnMultiplicacao = Button(janela, text="*", command= lambda: multiplicacao())
btnDivisao = Button(janela, text="/", command= lambda: divisao())
btnResultado = Button(janela, text="=", command= lambda: resultado())
btnLimpar = Button(janela, text="Limpar", command= lambda: limpar())

btnAdicao.grid(row=1 ,column=3, ipadx=20, ipady=10)
btnSubtracao.grid(row=2 ,column=3, ipadx=20, ipady=10)
btnMultiplicacao.grid(row=3 ,column=3, ipadx=20, ipady=10)
btnDivisao.grid(row=4 ,column=3, ipadx=20, ipady=10)
btnResultado.grid(row=4 ,column=2, ipadx=20, ipady=10)
btnLimpar.grid(row=4, column=1, ipadx=20, ipady=10)

janela.mainloop()
numero = list(input("Digite um numero binario:"))

valor = 0

for x in range(len(numero)):
    print(numero, x)
    digito = numero.pop()
    if digito == "1":
        valor = valor + pow(2, x)
print(f"O valor decimal é {valor}")
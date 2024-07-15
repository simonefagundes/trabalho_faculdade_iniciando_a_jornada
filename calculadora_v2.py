def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        print("Não é possível dividir por zero")
    else:
        return a / b

a = float(input("Digite um número: "))
b = float(input("Digite outro número: ")) 
selecao = input("Selecione uma operação: Adicao, Subtracao, Multiplicacao, Divisao: ")

def calculadora(a, b, selecao):
    if selecao == "Adicao":
        return adicao(a, b)
    elif selecao == "Subtracao":
        return subtracao(a, b)
    elif selecao == "Multiplicacao":
        return multiplicacao(a, b)
    elif selecao == "Divisao":
        return divisao(a, b)
    else:
        print("Operação inválida")

resultado = calculadora(a, b, selecao)
print("Resultado:", resultado)




saida = ""
while saida.lower() != "n":
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    selecao = input("Selecione uma operação: Adicao, Subtracao, Multiplicacao, Divisao: ")
    
    resultado = calculadora(a, b, selecao)
    if resultado is not None:
        print(f"Resultado da operação: {resultado}")
    
    saida = input("Deseja continuar (S/N)? ")
    while saida.lower() not in {"s", "n"}:
        saida = input("Opção inválida. Deseja continuar (S/N)? ")

print("Programa encerrado.")

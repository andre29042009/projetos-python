import logo

print(logo.logo)
again = ""
def adicao(n1, n2, conta):
    conta += n1 + n2
    return conta

def subtracao(n1, n2, conta):
    conta += n1 - n2
    return conta

def multiplicacao(n1, n2, conta):
    conta += n1 * n2
    return conta

def divisao(n1, n2, conta):
    conta += n1 / n2
    return conta

while True:
    calculo = 0
    number1 = int(input("Digite o primeiro número:\n"))
    operacao = input("Digite a operacao:\n")
    number2 = int(input("Digite o segundo número:\n"))

    if operacao == "+":
        calculo = adicao(number1, number2, calculo)
    elif operacao == "-":
        calculo = subtracao(number1, number2, calculo)
    elif operacao == "*":
        calculo = multiplicacao(number1, number2, calculo)
    elif operacao == "/":
        calculo = divisao(number1, number2, calculo)
    print(f"O resultado é {calculo}")
    while True:
        again = input("Deseja continuar? [Y/N]").upper()
        if again == "Y":
            break
        elif again != "N":
            continue
        else: 
            break
    if again == "Y":
        continue
    else:
        break
import logo

print(logo.logo)


def calculadora():
    again = ""
    calculo = 0
    while  True:
        firstNumber = int(input("Qual o primeiro número? \n"))
        secondNumber = int(input("Qual o segundo número? \n"))
        while True:
            operation = input("Qual a operação? \n + \n - \n * \n /\n")
            if operation not in ["+", "-", "*", "/"]:
                continue
            else:
                break
        if operation == "+":
            calculo = firstNumber + secondNumber
        elif operation == "-":
            calculo = firstNumber - secondNumber
        elif operation == "*":
            calculo = firstNumber * secondNumber
        elif operation == "/":
            calculo = firstNumber / secondNumber
        
        print(f"O resultado é {calculo}")
        while again != "Y" or again != "N":
            again = input("Deseja fazer outro calculo ? [Y/N]\n").upper()

            if again == "Y" or again == "N":
                break
            else:
                continue
        if again == "Y":
            continue
        else:
            break
calculadora()



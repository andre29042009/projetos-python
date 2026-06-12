MENU = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "preço": 1.5,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leite": 150,
            "cafe": 24,
        },
        "preço": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leite": 100,
            "cafe": 24,
        },
        "preço": 3.0,
    }
}

resources = {
    "agua": 300,
    "leite": 200,
    "cafe": 100,
}

def verificarEstoque(item, quantEstoque, quantItem):
    if quantEstoque >= quantItem:
        return True
    return f"Quantidade de {item} insuficiente."
def diminuirEstoque (quantEstoque, quantItem):
    return quantEstoque - quantItem
def aumentarEstoque (quantEstoque, quantItem):
    return quantEstoque + quantItem
money = 0
on = True
choice = ""
cost = 0
while on:
    moneyUser = 0
    choice = ""
    while not choice in ["espresso", "latte", "cappuccino", "off", "relatorio", "adm"]:
        choice = input("O que você gostaria? (espresso/latte/cappuccino) (digite adm para comandos privilegiados)\n").lower()
    if choice == "espresso":
        cost = MENU["espresso"]["preço"]
    elif choice == "latte":
        cost = MENU["latte"]["preço"]
    elif choice == "cappuccino":
        cost = MENU["cappuccino"]["preço"]
    elif choice == "adm":
        comandosAdm = ""
        while not comandosAdm in ["off", "relatorio", "adicionar"] :
            comandosAdm = input("Digite 'relatorio' para acessar o relatório de estoque e dinheiro obtido. \nDigite 'off' para desligar a máquina\nDigite 'adicionar' para adicionar recursos na máquina.\n").lower()
        if comandosAdm == "relatorio":
            allResources = ""
            for n in resources:
                allResources += f"{n.capitalize()}: {resources[n]}ml\n"
            allResources += f"Dinheiro: {money}R$"
            print(allResources)
        elif comandosAdm == "off":
            print("Máquina desligada.")
            break
        elif comandosAdm == "adicionar":
            recurso = ""
            quantRecurso = 0
            while recurso not in ["agua", "cafe", "leite"]:
                recurso = input("Deseja adicionar qual recurso?\n 'agua' para água\n 'cafe' para café\n 'leite' para leite\n").lower()
            for z in resources:
                if z == recurso:
                    while quantRecurso < 1 or quantRecurso >= 1000:
                        try:
                            quantRecurso = int(input("Valor que deseja adicionar : 1-999(ml)\n"))
                        except ValueError:
                            print("Digite apenas o número.")
                    resources[z] = aumentarEstoque(resources[z], quantRecurso)
                    print(f"Valor adicionado.\nValor atual de {recurso}: {resources[z]}ml")

    if choice in ["espresso", "cappuccino", "latte"]:
        autorizar = []
        for n in MENU[choice]["ingredientes"]:
            autorizar.append(verificarEstoque(n, resources[n], MENU[choice]["ingredientes"][n]))

        estoqueSuficiente = "sim"
        for a in autorizar:
            if a != True:
                print (a)
                estoqueSuficiente = "nao"

        if estoqueSuficiente == "sim":
            print(f"O {choice} custa {cost}R$")
            while True:
                try:
                    moneyUser += float(input("Digite o quanto deseja depositar: "))
                    break
                except ValueError:
                    print("Digite um valor numérico")
            while moneyUser < MENU[choice]["preço"]:
                print(f"Valor atual: {moneyUser}R$ \nValor do {choice}: {MENU[choice]["preço"]}R$")
                while True:
                    try:
                        moneyUser += float(input("Digite o quanto deseja depositar: "))
                        break
                    except ValueError:
                        print("Digite um valor numérico")
            money += MENU[choice]["preço"]
            print(f"Quantidade de dinheiro atual: {moneyUser}R$")
            print(f"Seu {choice} está pronto!")
            if moneyUser > MENU[choice]["preço"]:
                troco = moneyUser - MENU[choice]["preço"]
                print(f"Aqui está o seu troco: {troco}")
            for a in MENU[choice]["ingredientes"]:
                resources[a] = diminuirEstoque(resources[a], MENU[choice]["ingredientes"][a])

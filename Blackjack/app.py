import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
again = ""
def new_score(currentScore, allCards):
    currentScore = 0
    for card in allCards:
        currentScore += card
    return currentScore
while True:
    again = input("Deseja jogar BlackJack? [Y/N]? ").upper()
    if again == "Y":
        userCurrentScore = 0
        computerCurrentScore = 0
        userCards = []
        print(art.logo)
        userCards.append(random.choice(cards))
        userCards.append(random.choice(cards))
        computerCards = [random.choice(cards), random.choice(cards)]
        userCurrentScore = new_score(userCurrentScore, userCards)
        computerCurrentScore = new_score(computerCurrentScore, computerCards)
        print(f"Suas cartas: {userCards}, pontuação atual: {userCurrentScore}")
        print(f"A primeira carta do computador: {userCards[0]}")

        while True:
            getPass = input("Deseja pegar outra carta [Y] ou passar [N]: ").upper()
            if getPass == "Y":
                userCards.append(random.choice(cards))
                userCurrentScore = new_score(userCurrentScore, userCards)
                if userCurrentScore > 21 and (11 in userCards):
                    for i, n in enumerate(userCards):
                        if n == 11:
                            userCards[i] = 1
                            userCurrentScore = new_score(userCurrentScore, userCards)
                            break
                if computerCurrentScore < 18:
                    computerCards.append(random.choice(cards))
                    computerCurrentScore = new_score(computerCurrentScore, computerCards)
                if computerCurrentScore > 21 and (11 in computerCards):
                    for i, n in enumerate(computerCards):
                        if n == 11:
                            computerCards[i] = 1
                            computerCurrentScore = new_score(computerCurrentScore, computerCards)
                            break

                print(f"Suas cartas: {userCards}, pontuação atual: {userCurrentScore}")
                print(f"Mão atual do computador (última carta não visível): {computerCards[:-1]}")
                if userCurrentScore > 21:
                    break
                if computerCurrentScore > 21:
                    break
            else:
                while computerCurrentScore < 18:
                    computerCards.append(random.choice(cards))
                    computerCurrentScore = new_score(computerCurrentScore, computerCards)
                break
        if userCurrentScore > 21 and computerCurrentScore > 21:
            print(f"Tanto você, quanto o computador perderam. As pontuações foram {userCurrentScore, computerCurrentScore}, respectivamente")
        elif userCurrentScore > 21:
            print(f"Você perdeu. {userCurrentScore} passou de 21.")
        elif computerCurrentScore > 21:
            print(f"O computador perdeu. {computerCurrentScore} passou de 21.")
        elif userCurrentScore > computerCurrentScore:
            print(f"Você ganhou!\n Sua pontuação: {userCurrentScore} \n Pontuação do computador: {computerCurrentScore}")
        elif userCurrentScore < computerCurrentScore:
            print(f"Você perdeu.\n Sua pontuação: {userCurrentScore} \n Pontuação do computador: {computerCurrentScore}")
        elif userCurrentScore == computerCurrentScore:
            print(f"Você empatou.\n Sua pontuação: {userCurrentScore} \n Pontuação do computador: {computerCurrentScore}")

    else:
        break

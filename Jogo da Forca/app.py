import arts
import random
import words
while True:
    print("Bem-vindo ao Jogo da Forca!\n")
    print(arts.logo)
    word = random.choice(words.word_list)
    display = ""

    correct_letters = []
    all_letters = []
    game_over = False
    hangman = 0
    lives = len(arts.stages) - 1
    while not game_over:
        guess = input("Digite uma letra: ").lower()
        display = ""

        if guess not in word and guess not in all_letters:
            hangman += 1
            print("A letra escolhida: ", guess.upper(), " não está na palavra.")
            lives -= 1
            print(f"Ainda te restam {lives} vidas")

        elif guess in all_letters:
            print("Você já tentou essa letra: ", guess.upper(), ". Tente outra")
        if guess in word and guess not in all_letters:
            print("A letra escolhida: ", guess.upper(), " está na palavra. Parabéns.")


        for letter in word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
        if guess not in all_letters:
            all_letters.append(guess)

        print(arts.stages[hangman])
        print(display)
        if "_" not in display:
            print("**********VOCÊ GANHOU**********")
            game_over = True
        elif arts.stages[hangman] == arts.stages[-1]:
            print(f"A palavra era: {word}")
            print("**********VOCÊ PERDEU**********")
            game_over = True
            
    again = input("Deseja continuar jogando[S/N]?").upper()
    if again == "N":
        break
    elif again == "S":
        continue
    else:
        print("Não consegui entender o que você disse, vou considerar que deseja parar de jogar.")
        break



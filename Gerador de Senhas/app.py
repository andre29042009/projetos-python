import random
import characters

print("Bem-vindo ao gerador de senhas!")

num_letters = int(input("Quantas letras deseja na sua senha?\n"))
num_numbers = int(input("Quantos números deseja na sua senha?\n"))
num_symbols = int(input("Quantos símbolos deseja na sua senha?\n"))

password_list =[]

for letter in range(0, num_letters):
    password_list.append(random.choice(characters.letters))
for number in range(0, num_numbers):
    password_list.append(random.choice(characters.numbers))
for symbol in range(0, num_symbols) :
    password_list.append(random.choice(characters.symbols))

random.shuffle(password_list)


password_final = ""
for n in password_list:
    password_final += n
print(f"Sua senha: {password_final}")
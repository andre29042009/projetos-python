import arts

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(arts.logo)

def caesar(original_text, shift_amount, encode_or_decode):
        output_text = ""

        if encode_or_decode == "decode":
            shift_amount *= -1

        for letter in original_text:
            if letter not in alphabet:
                output_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
        print(f"Here is the {encode_or_decode}d result: {output_text}")

while True:
    direction = input("Digite 'encode' para criptografar, digite 'decode' para descriptografar:\n").lower()
    text = input("Digite o texto:\n").lower()
    shift = int(input("Digite o número de deslocamento:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    forContinue = input("Deseja continuar? [S/N]?").upper()
    if forContinue == "S":
        continue
    else:
        break

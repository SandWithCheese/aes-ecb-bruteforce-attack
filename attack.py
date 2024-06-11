import requests
from string import printable
from colorama import Fore, Style


def encrypt(plaintext):
    plain_hex = plaintext.encode().hex()
    url = "http://127.0.0.1:5000/encrypt/" + plain_hex
    r = requests.get(url)
    r_data = r.json()
    return r_data.get("ciphertext", None)


def pad_flag_guess(guess):
    padding = "A" * (16 - len(guess) % 16)
    padded_guess = padding + guess + padding

    return padded_guess


if __name__ == "__main__":
    flag = ""

    counter = 0
    while True:
        for l in printable:
            counter += 1
            flag_guess = flag + l
            padded_guess = pad_flag_guess(flag_guess)
            ciphertext = encrypt(padded_guess)

            guess_output_size = 2 * ((16 - len(flag_guess) % 16) + len(flag_guess))

            encrypted_guess = ciphertext[:guess_output_size]
            encrypted_flag = ciphertext[guess_output_size : guess_output_size * 2]

            print("Ciphertext:")
            for i in range(0, len(ciphertext), guess_output_size):
                cipher_block = ciphertext[i : i + guess_output_size]
                if cipher_block == encrypted_flag and cipher_block == encrypted_guess:
                    for j in range(0, len(cipher_block), 32):
                        print(Fore.YELLOW + cipher_block[j : j + 32])
                elif cipher_block == encrypted_flag:
                    for j in range(0, len(cipher_block), 32):
                        print(Fore.RED + cipher_block[j : j + 32])
                elif cipher_block == encrypted_guess:
                    for j in range(0, len(cipher_block), 32):
                        print(Fore.GREEN + cipher_block[j : j + 32])
                else:
                    print(Fore.BLUE + cipher_block)
                print(Style.RESET_ALL, end="")

            print(f"Padded guess: {padded_guess}")
            print(f"Guessed character: {l}")
            if encrypted_guess == encrypted_flag:
                flag = flag_guess
                print(f"Flag: {flag}")
                print()
                break

            print()
        else:
            break

    print(f"Total requests: {counter}")
    print(f"Flag: {flag}")
    print(len(printable))

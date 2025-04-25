def encryption_str(text, n, m):
    new_str = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                if 'a' <= char <= 'm':
                    new_char = chr((ord(char) - ord('a') + n * m) % 26 + ord('a'))
                else:
                    new_char = chr((ord(char) - ord('a') - (n + m)) % 26 + ord('a'))
            else:
                if 'A' <= char <= 'M':
                    new_char = chr((ord(char) - ord('A') - n) % 26 + ord('A'))
                else:
                    new_char = chr((ord(char) - ord('A') + m ** 2) % 26 + ord('A'))
            new_str += new_char
        else:
            new_str += char
    return new_str


def decrypt_str(text, n, m):
    new_str = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                if 'a' <= char <= 'm':
                    new_char = chr((ord(char) - ord('a') - n * m + 26) % 26 + ord('a'))
                else:
                    new_char = chr((ord(char) - ord('a') + (n + m)) % 26 + ord('a'))
            else:
                if 'A' <= char <= 'M':
                    new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
                else:
                    new_char = chr((ord(char) - ord('A') - m ** 2 + 26) % 26 + ord('A'))
            new_str += new_char
        else:
            new_str += char
    return new_str


def encrypt_content(text, n, m):
    return encryption_str(text, n, m)


def decrypt_content(text, n, m):
    return decrypt_str(text, n, m)


def check_decrypt(original_txt, decrypted_txt):
    return original_txt == decrypted_txt


def main():
    try:
        n = int(input("please enter n: "))
        m = int(input("please enter m: "))

        original_txt = "The quick brown fox jumps over the lazy dog beneath the shady willows. The dog, startled from his peaceful afternoon nap, quickly rises and chases after the mischievous fox. Through vibrant meadows and past buzzing beehives they race, disturbing a flock of quails that scatter into the crisp autumn sky. The fox, quite pleased with his clever prank, dashes into his cozy underground den while the dog, now exhausted from the zealous pursuit, returns to his favorite spot under the whispering branches to resume his quiet slumber."

        encrypted_txt = encrypt_content(original_txt, n, m)
        decrypted_text = decrypt_content(encrypted_txt, n, m)

        is_correct = check_decrypt(original_txt, decrypted_text)
        print(f"check decryption correct: {is_correct}")

        print("original_txt:", original_txt)
        print("encrypted_txt:", encrypted_txt)
        print("decrypted_text:", decrypted_text)

    except ValueError:
        print("please enter a valid integer for n and m.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
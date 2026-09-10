"""Interactive Caesar cipher program for Problem 5."""


def caesar_cipher(text, shift):
    """Return text encrypted by shifting alphabetic characters by *shift*."""
    encrypted = ""

    for index in range(len(text)):
        character = text[index]

        if "a" <= character <= "z":
            encrypted += chr((ord(character) - ord("a") + shift) % 26 + ord("a"))
        elif "A" <= character <= "Z":
            encrypted += chr((ord(character) - ord("A") + shift) % 26 + ord("A"))
        else:
            encrypted += character

    return encrypted


def caesar_decipher(ciphertext, shift):
    """Return the original text from a Caesar-encrypted string."""
    return caesar_cipher(ciphertext, -shift)


def letter_frequency(text):
    """Count each letter in text, ignoring case and non-alphabetic characters."""
    frequencies = {}

    for index in range(26):
        frequencies[chr(ord("a") + index)] = 0

    for index in range(len(text)):
        character = text[index].lower()
        if "a" <= character <= "z":
            frequencies[character] += 1

    return frequencies


def print_frequency(frequencies):
    """Print only letters that appear in the alphabetical frequency breakdown."""
    print("Letter frequency:")
    for index in range(26):
        letter = chr(ord("a") + index)
        if frequencies[letter] > 0:
            print(letter + ":", frequencies[letter])


def main():
    """Run a two-option terminal menu for the Caesar cipher program."""

    while True:
        print("\nCaesar Cipher Menu")
        print("1. Enter a message to encrypt")
        print("2. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter a message: ")
            while True:
                try:
                    shift = int(input("Enter a shift value: "))
                    break
                except ValueError:
                    print("Please enter a whole-number shift value.")

            ciphertext = caesar_cipher(message, shift)
            print("Encrypted text:", ciphertext)
            print_frequency(letter_frequency(message))
            print("Decrypted text:", caesar_decipher(ciphertext, shift))
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Please choose 1 or 2.")


if __name__ == "__main__":
    main()

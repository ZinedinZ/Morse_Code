
morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',  'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '.': '.-.-.-', ',': '--..--', '?': '..--..',  '!': '-.-.--',  '-': '-....-',  '/': '-..-.',
              '(': '-.--.', ')': '-.--.-',  '"': '.-..-.',  "'": '.----.',  '+': '.-.-.', '=': '-...-',
              '@': '.--.-.', '$': '...-..-', '&': '.-...', '_': '..--.-'
              }


def translate(users_choice):
    # Using list comprehension to split word
    splitted_word = [letter for letter in users_choice]
    morse_word = ""
    for letter in splitted_word:
        morse_word += morse_code[letter]
    print(f"Your word in morse code is: {morse_word}")


loop = True

while loop:
    word = input("What is word that you want to translate to Morse Code: ").upper()

    try:
        translate(word)
    except KeyError:
        print("Wrong input, some of your letters doesn't exist in Morse Code")

    # Asking user to translate more words
    again = input("Do you want to translate again? if yes type 'y', if no type 'n' ").lower()
    if again == "y":
        pass
    elif again == "n":
        loop = False
    else:
        print("Wrong input, please type 'Y' for yes and 'n' for no")

import sys


class MorseException(Exception):
    pass


j = {'A': '.-', 'B': '-...',
     'C': '-.-.', 'D': '-..', 'E': '.',
     'F': '..-.', 'G': '--.', 'H': '....',
     'I': '..', 'J': '.---', 'K': '-.-',
     'L': '.-..', 'M': '--', 'N': '-.',
     'O': '---', 'P': '.--.', 'Q': '--.-',
     'R': '.-.', 'S': '...', 'T': '-',
     'U': '..-', 'V': '...-', 'W': '.--',
     'X': '-..-', 'Y': '-.--', 'Z': '--..',
     '1': '.----', '2': '..---', '3': '...--',
     '4': '....-', '5': '.....', '6': '-....',
     '7': '--...', '8': '---..', '9': '----.',
     '0': '-----', ', ': '--..--', '.': '.-.-.-',
     '?': '..--..', '/': '-..-.', '-': '-....-',
     '(': '-.--.', ')': '-.--.-'}


def decode(dictionary):
    print(f'Instructions:\n\
    {"".center(15, "*")}\n\
    ! to quit\n\
    empty string to reverse translation\n\
    enjoy)\n')
    while True:
        text = input("Please provide some text to convert it into morze code: ").upper().split()
        if text == ['!']:
            sys.exit()
        elif text == '':
            pass
        else:
            for char in text:
                try:
                    print(" ".join([dictionary[letter] for letter in char]))
                except KeyError:
                    return 0
        g = input('Input some morze code, enter to return to reverse translation: ').split()
        if g == ['!']:
            print('Exit with ')
            sys.exit()
        elif g == '':
            continue
        else:
            for char in g:
                try:
                    print(" ".join(dictionary[letter] for letter in char))
                except KeyError:
                    return 0


def main():
    do = decode(j)
    if do == 1:
        print("Process finished with exit code 0")
    else:
        raise MorseException("Unbound val")


if __name__ == '__main__':
    main()

import sys

def check_message(message):
    for c in message:
        if not c.isalnum() and c != ' ':
            return False
    return True

def encode_morse(message):
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }
    upper_message = message.upper()
    return ' '.join([MORSE_CODE_DICT[c] for c in upper_message])

def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return
    if (not check_message(sys.argv[1])):
        print("AssertionError: the arguments are bad")
        return
    print(encode_morse(sys.argv[1]))

if __name__ == "__main__":
    main()

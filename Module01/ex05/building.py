import sys


def is_punctuation(c):
    return not (c.isalpha() or c.isdigit() or c.isspace())


def string_analyzer(value):
    """This function analyzes a string and prints its characters counts:
- upper letters,
- lower letters,
- punctuation marks,
- spaces and digits."""
    print(f'The text contains {len(value)} characters:')
    print(f'{sum(1 for c in value if c.isupper())} upper letters')
    print(f'{sum(1 for c in value if c.islower())} lower letters')
    print(f'{sum(1 for c in value if is_punctuation(c))} punctuation marks')
    print(f'{sum(1 for c in value if c.isspace())} spaces')
    print(f'{sum(1 for c in value if c.isdigit())} digits')


def main():
    value = ''
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    elif len(sys.argv) == 2:
        value = sys.argv[1]
    else:
        while value == '':
            value = input("What is the text to count?\n")
    string_analyzer(value)


if __name__ == "__main__":
    main()

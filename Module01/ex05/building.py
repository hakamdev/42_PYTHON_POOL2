import sys


def is_punctuation(c):
    """Checks if a character is a punctuation mark."""
    return not (c.isalpha() or c.isdigit() or c.isspace())


def string_analyzer(value: str):
    """Analyzes a string and prints its characters counts:
- upper letters,
- lower letters,
- punctuation marks,
- spaces,
- digits.
"""

    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    spaces_count = 0
    digits_count = 0

    for c in value:
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1
        elif is_punctuation(c):
            punctuation_count += 1
        elif c.isspace():
            spaces_count += 1
        elif c.isdigit():
            digits_count += 1

    print(f'The text contains {len(value)} characters:')
    print(f'{upper_count} upper letters')
    print(f'{lower_count} lower letters')
    print(f'{punctuation_count} punctuation marks')
    print(f'{spaces_count} spaces')
    print(f'{digits_count} digits')


def main():
    value = ''
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    elif len(sys.argv) == 2:
        value = sys.argv[1]
    else:
        print("What is the text to count?")
        value = sys.stdin.readline()
    string_analyzer(value)


if __name__ == "__main__":
    main()

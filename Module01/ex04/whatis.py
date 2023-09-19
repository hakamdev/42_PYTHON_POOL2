import sys


def main():
    if len(sys.argv) == 1:
        return
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    try:
        num = int(sys.argv[1])
        print("I'm Even." if num % 2 == 0 else "I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")


main()

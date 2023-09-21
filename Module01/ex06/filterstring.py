import sys
from ft_filter import ft_filter

def check_args(args):
    if len(args) != 3:
        return (False, 0)
    try:
        n = int(args[2])
        return (True, n)
    except ValueError:
        return (False, 0)

def main():
    (success, n) = check_args(sys.argv)
    if not success:
        print("AssertionError: the arguments are bad")
        return
    words = sys.argv[1].split()
    filtered_words = ft_filter(lambda x: len(x) >= n, words)
    print(filtered_words)

if __name__ == "__main__":
    main()

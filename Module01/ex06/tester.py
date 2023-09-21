from ft_filter import ft_filter

def main():
    print("None:                      ", ft_filter(None, [0, 1, False, 2, True, '', 3, 'a', 's', 34, None]))
    print("not c.isalpha():           ", ft_filter(lambda c: not c.isalpha(), [".",",",";", "$", "a", "b", "c", "d", "e", "f", "g"]))
    print("c.isalpha():               ", ft_filter(lambda c: c.isalpha(), [".",",",";", "$", "a", "b", "c", "d", "E", "F", "G"]))
    print("c.isalpha() and c.isupper()", ft_filter(lambda c: c.isalpha() and c.isupper(), [".",",",";", "$", "a", "b", "c", "d", "E", "F", "G"]))
    print("__doc__:                   ", filter.__doc__ == ft_filter.__doc__);
    print(ft_filter.__doc__)

if __name__ == "__main__":
    main()
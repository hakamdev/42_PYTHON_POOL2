def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list based on the start and end indexes.
    Args:
        family (list): 2D list.
        start (int): Start index.
        end (int): End index.
    """
    # Error handling
    if type(family) is not list:
        print("AssertionError: family is not a list")
    if len(family) > 0 and type(family[0]) is not list:
        print("AssertionError: family is not a 2D list")
    if type(start) is not int or type(end) is not int:
        print("AssertionError: Invalid argument")

    # handle family
    columns = len(family)
    rows = 0 if columns == 0 else len(family[0])
    print(f"My shape is : ({columns}, {rows})")

    # slice and handle new_family
    new_family = family[start: end]
    new_columns = len(new_family)
    new_rows = 0 if new_columns == 0 else len(new_family[0])
    print(f"My new shape is : ({new_columns}, {new_rows})")
    return new_family

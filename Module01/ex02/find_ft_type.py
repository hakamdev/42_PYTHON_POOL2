def all_thing_is_obj(object: any) -> int:
    primives = [int, float, bool]

    # if object is a string
    if object.__class__ == str:
        print(f'{object} is in the kitchen : {object.__class__}')
    # if object is not an object type
    elif object.__class__ in primives:
        print('Type not found')
    # if object is an object type
    else:
        print(f'{object.__class__.__name__.capitalize()} : {object.__class__}')
    return 42

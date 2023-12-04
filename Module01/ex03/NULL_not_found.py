def NULL_not_found(object: any) -> int:
    labels = {'NoneType': 'Nothing', 'int': 'Zero',
              'str': 'Empty', 'bool': 'Fake', 'float': 'Cheese'}
    # NaN is the only value that is not equal to itself
    is_nan = object != object
    # 0, '', False, None are all falsy when converted to bool
    is_falsy = not bool(object)

    if is_nan or is_falsy:
        print(
            f'{labels[object.__class__.__name__]}: {object} {object.__class__}'
            )
        return 0
    else:
        print('Type not Found')
    return 1

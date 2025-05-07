def validate_args(*args: any) -> bool:
    """Validate if all args are numbers.
"""
    for num in args:
        if not num.__class__ in [int, float]:
            return False
    return True


def sort_args(*args: any) -> list:
    """Sort the list of numbers.
"""
    s_args = list(args)
    length = args_length(s_args)
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if s_args[i] > s_args[j]:
                s_args[i], s_args[j] = s_args[j], s_args[i]
            j += 1
        i += 1
    return s_args


def args_sum(args: list) -> float:
    """Calculate the sum of a list of numbers.
"""
    sum = 0
    for num in args:
        sum += num
    return sum


def args_length(args: list) -> int:
    """Calculate the length of args Tuple.
"""
    length = 0
    for _ in args:
        length += 1
    return length


def kwargs_length(**kwargs: any) -> int:
    """Calculate the length of kwargs Dict.
"""
    length = 0
    for _ in kwargs:
        length += 1
    return length


def caluclate_mean(args: list) -> float:
    """Calculate the mean of a list of numbers.
"""
    return args_sum(args) / args_length(args)


def calculate_median(args: list) -> float:
    """Calculate the median of a list of numbers.
"""
    length = args_length(args)
    if length % 2 == 0:
        return (args[length // 2] + args[length // 2 - 1]) / 2
    return args[length // 2]


def calculate_upper_quartile(args: list) -> float:
    """Calculate the upper quartile (75%) of a list of numbers.
"""
    length = args_length(args)
    index = length * (3 / 4)
    print(index)
    if index % 1 != 0:
        return args[int(index)]
    return (args[int(index)] + args[int(index) - 1]) / 2


def calculate_lower_quartile(args: list) -> float:
    """Calculate the lower quartile (25%) of a list of numbers.
"""
    length = args_length(args)
    index = length / 4
    print(index)
    if index % 1 != 0:
        return args[int(index)]
    return (args[int(index)] + args[int(index) - 1]) / 2


def calculate_variance(args: list) -> float:
    """Calculate the variance of a list of numbers.
"""
    pass


def calculate_standard_deviation(args: list) -> float:
    """Calculate the standard deviation of a list of numbers.
"""
    pass


# mean : 95.6
# median : 42
# quartile : [11.0, 64.0]
# -----
# std : 17982.70124086944
# var : 323377543.9183673
def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculate the mean, median, quartile, variance, 
and standard deviation of a list of numbers
"""
    if not validate_args(*args):
        print("AssertionError: args must be numbers.")
        return
    args_list = sort_args(*args)
    print(args_list)

    print("Mean:", caluclate_mean(args_list))
    print("Median:", calculate_median(args_list))
    print("Upper Quartile:", calculate_upper_quartile(args_list))
    print("Lower Quartile:", calculate_lower_quartile(args_list))
    print("Variance:", calculate_variance(args_list))
    print("Standard Deviation:", calculate_standard_deviation(args_list))

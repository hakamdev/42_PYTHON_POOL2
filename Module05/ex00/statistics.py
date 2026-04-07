def validate_args(*args: any) -> bool:
    """Validate if all args are numbers.
"""
    for num in args:
        if num.__class__ not in [int, float]:
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
    if index % 1 != 0:
        return float(args[int(index)])
    return float(args[int(index)] + args[int(index) - 1] / 2)


def calculate_lower_quartile(args: list) -> float:
    """Calculate the lower quartile (25%) of a list of numbers.
"""
    length = args_length(args)
    index = length / 4
    if index % 1 != 0:
        return float(args[int(index)])
    return float(args[int(index)] + args[int(index) - 1] / 2)


def calculate_quartiles(args: list) -> list:
    """Calculate the upper and lower quartiles of a list of numbers.
"""
    return [calculate_lower_quartile(args), calculate_upper_quartile(args)]


def calculate_variance(args: list) -> float:
    """Calculate the variance of a list of numbers.
"""
    mean = caluclate_mean(args)
    variance = 0
    for num in args:
        variance += (num - mean) ** 2
    return variance / args_length(args)


def calculate_standard_deviation(args: list) -> float:
    """Calculate the standard deviation of a list of numbers.
"""
    return calculate_variance(args) ** 0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculate the mean, median, quartile, variance,
and standard deviation of a list of numbers
"""
    args_len = args_length(args)
    args_valid = True
    if not (validate_args(*args) and args_len > 0):
        args_valid = False
    for key, value in kwargs.items():
        if (not args_valid):
            print("ERROR")
            continue
        args_list = sort_args(*args)
        if value == "mean":
            print("mean :", caluclate_mean(args_list))
        elif value == "median":
            print("median :", calculate_median(args_list))
        elif value == "quartile":
            print("quartile :", calculate_quartiles(args_list))
        elif value == "std":
            print("std :", calculate_standard_deviation(args_list))
        elif value == "var":
            print("var :", calculate_variance(args_list))

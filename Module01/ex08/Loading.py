# import os

def get_percentage(elapsed: float, total: float) -> float:
    return int((elapsed / total) * 100)

# def get_bar_max_width(number_width: int) -> int:
#     return os.get_terminal_size().columns - get_info_width(number_width)

def get_bar_max_width(number_width: int) -> int:
    return 179 - get_info_width(number_width)


def get_bar_width(percentage: int, max_width: int) -> int:
    return int((percentage / 100) * max_width)


def get_info_width(number_width: int) -> int:
    return 10 + 24 + number_width * 2


def get_info(percentage: int, total: int, number_width: int, available_space: int) -> str:
    return f"| {percentage:{number_width}}/{total:{number_width}}"[0:available_space]


def ft_tqdm(lst: range) -> None:
    number = 1
    for item in lst:
        number_width = len(str(len(lst)))
        percentage = get_percentage(number, len(lst))
        max_bar_width = get_bar_max_width(number_width)
        bar_width = get_bar_width(percentage, max_bar_width)
        print(f"{percentage:3}%|{'█' * bar_width:{max_bar_width}}{get_info(number, len(lst), number_width, get_info_width(number_width))}", end="\r")
        number += 1
        yield item

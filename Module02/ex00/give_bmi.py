def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI (Body Mass Index) of each pair of height and weight from lists provded as arguments.
    Args:
        height (list[int | float]): List of heights.
        weight (list[int | float]): List of weights.

    Returns:
        list[int | float]: List of BMIs.
    """
    if type(height) != list or type(weight) != list:
        print("Error: invalid args")
        return []
    if not (len(height) == len(weight)):
        print("Error: height and weight lists must have the same length")
        return []
    length = len(height)
    bmi = []
    for i in range(length):
        try:
            bmi.append(weight[i] / (height[i] ** 2))
        except ZeroDivisionError:
            pass
        except TypeError:
            pass
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Applies a limit to a list of BMI values.
    Args:
        bmi (list[int | float]): List of BMIs.
        limit (int): Limit to apply.

    Returns:
        list[bool]: List of booleans.
    """
    bmi_limit = []
    if type(limit) != int or type(bmi) != list:
        print("Error: invalid args")
        return bmi_limit

    for i in range(len(bmi)):
        if not (type(bmi[i]) == int or type(bmi[i]) == float):
            print("Error: bmi arg contains values with invalid types")
            return []
        bmi_limit.append(bmi[i] > limit)
    return bmi_limit

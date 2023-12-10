def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI (Body Mass Index) of each pair of height and weight
    from lists provded as arguments.
    Args:
        height (list[int | float]): List of heights.
        weight (list[int | float]): List of weights.

    Returns:
        list[int | float]: List of BMIs.
    """
    try:
        if type(height) is not list or type(weight) is not list:
            print("AssertionError: invalid args")
            return []
        if not (len(height) == len(weight)):
            print(
                "AssertionError: height and weight must have the same length")
            return []
        if len(height) == 0:
            return []
        length = len(height)
        bmi = []
        for i in range(length):
            bmi.append(weight[i] / (height[i] ** 2))
        return bmi
    except ZeroDivisionError:
        print("AssertionError: division by zero")
    except TypeError:
        print("AssertionError: invalid types in height or weight lists")
    except Exception:
        print("AssertionError: unknown error")
    return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Applies a limit to a list of BMI values.
    Args:
        bmi (list[int | float]): List of BMIs.
        limit (int): Limit to apply.

    Returns:
        list[bool]: List of booleans.
    """
    bmi_limit = []
    if type(limit) is not int or type(bmi) is not list:
        print("AssertionError: invalid args")
        return bmi_limit

    for i in range(len(bmi)):
        if not (type(bmi[i]) is int or type(bmi[i]) is float):
            print("AssertionError: bmi arg contains values with invalid types")
            return []
        bmi_limit.append(bmi[i] > limit)
    return bmi_limit

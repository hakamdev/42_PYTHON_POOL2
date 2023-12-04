from give_bmi import give_bmi, apply_limit


def main():
    height = [1.70, "hakam", 1.65, 1.90, 1.75, 1.80]
    weight = [65, 80, 55, 100, 33, 70, 80]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 25))


if __name__ == "__main__":
    main()

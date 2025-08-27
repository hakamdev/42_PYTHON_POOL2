from S1E9 import Character


def main():
    try:
        hodor = Character("hodor")
        print(hodor.__dict__)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()

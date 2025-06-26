import random

def main():
    level = get_level()
    problems_given = 0
    score = 0

    while problems_given < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y

        for attempt in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == correct:
                    score += 1
                    break
                else:
                    print("EEE")

            except ValueError:
                print("EEE")

            else:
                print(f"{x} + {y} = {correct}")
        problems_given += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:                       
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
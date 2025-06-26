def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
            print(f"{gauge(percentage)}")

        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = map(int, fraction.split("/"))
    
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    
    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
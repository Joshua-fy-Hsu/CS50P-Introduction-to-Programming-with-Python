while True:
    try:
        num = input("Fraction: ").strip().split("/")
        x, y = int(num[0]), int(num[1])
        fuel = round(x / y * 100)
        
        if 99 <= fuel <= 100:
            print("F")
            break
        elif 0 <= fuel <= 1:
            print("E")
            break
        elif 1 < fuel < 99:
            print(f"{fuel}%")
            break
        else:
            pass

    except ValueError:
        pass

    except ZeroDivisionError:
        pass
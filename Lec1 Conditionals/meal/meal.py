def main():
    time = input("What time is it? ").strip()
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12<= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()
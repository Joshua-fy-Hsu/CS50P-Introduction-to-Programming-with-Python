def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    digit_found = False
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[0:2].isalpha():
        return False
    elif not s.isalnum():
        return False
    for i in range(len(s)):
        if s[i].isdigit():
            if not digit_found:
                if s[i] == "0":
                    return False
                digit_found = True
        else:
            if digit_found:
                return False
    return True

main()
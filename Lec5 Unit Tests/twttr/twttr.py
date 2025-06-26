def main():
    word = input("Input: ").strip()
    print(f"Output: {shorten(word)}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    shorten_word = ""

    for char in word:
        if char not in vowels:
            shorten_word += char

    return shorten_word



if __name__ == "__main__":
    main()

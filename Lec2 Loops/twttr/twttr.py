vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

text = input("Input: ")
print("Output: ", end = "")
for char in text:
    if char in vowels:
        char = ""
    print(char, end = "")
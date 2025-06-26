answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

new_answer = answer.strip().lower().replace(" ", "").replace("-", "")

if new_answer.isdigit():
    if int(new_answer) == 42:
        print("Yes")
    else:
        print("No")
elif new_answer == "fortytwo":
    print("Yes")
else:
    print("No")
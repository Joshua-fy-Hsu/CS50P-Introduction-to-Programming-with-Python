def main():
    str = input()
    convert(str)

def convert(text):
    text = text.replace(":)", "\U0001F642").replace(":(", "\U0001F641")
    print(text)

main()
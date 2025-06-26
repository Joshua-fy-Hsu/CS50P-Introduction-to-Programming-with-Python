from PIL import Image, ImageOps
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments  ")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    input = sys.argv[1]
    output = sys.argv[2]
    types = (".jpg", ".jpeg", ".png")

    if not input.endswith(types):
        sys.exit("Invalid input")
    elif not output.endswith(types):
        sys.exit("Invalid output")
    elif input.split(".")[1] != output.split(".")[1]:
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")

        with Image.open(input) as image:
            image = ImageOps.fit(image, shirt.size)
            image.paste(shirt, shirt)
            image.save(output)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
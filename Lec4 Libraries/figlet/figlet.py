from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
available_fonts = figlet.getFonts()

if len(sys.argv) not in [1, 3]:
    sys.exit("Invalid usage")

if len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    font_name = sys.argv[2]
    if font_name not in available_fonts:
        sys.exit("Invalid usage")
    figlet.setFont(font = font_name)
else:
    figlet.setFont(font = random.choice(available_fonts))

text = input("Input: ")
print(figlet.renderText(text))
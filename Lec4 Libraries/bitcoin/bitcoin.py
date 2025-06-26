import sys
import requests

try:
    response = requests.get("https://rest.coincap.io/v3/assets?apiKey=6a72473f6f0d5062f004534361ec34c3bba5ccae862681ce98b1c9fcaab0a462")
    data = response.json()
    current_price = float(data["data"][0]["priceUsd"])
except requests.RequestException:
    sys.exit()


try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
print(f"${n * current_price:,.4f}")
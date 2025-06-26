expression = input("Expression: ").strip()

x, y, z = expression.split(" ")

if y == "+":
    ans = float(x) + float(z)
    print(f"{ans:.1f}")
elif y == "-":
    ans = float(x) - float(z)
    print(f"{ans:.1f}")
elif y == "*":
    ans = float(x) * float(z)
    print(f"{ans:.1f}")
elif y == "/":
    ans = float(x) / float(z)
    print(f"{ans:.1f}")

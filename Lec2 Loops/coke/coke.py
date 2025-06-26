amount_due = 50
accepted_coin = [5, 10, 25]

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in accepted_coin:
        amount_due -= coin

change = abs(amount_due)
print(f"Change Owed: {change}")
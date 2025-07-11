amount = 50
while amount > 0:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert Coin: "))
    if coin not in [5, 10, 25]:
        continue
    amount -= coin

if amount == 0:
    print("Change Owed: 0")
else:
    print(f"Change Owed: {-amount}")

while True:
    try:
        fraction = input("Fraction: ").strip()
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y or x < 0 or y < 0:
            raise ValueError
        elif y == 0:
            raise ZeroDivisionError
        fuel = round(x/ y * 100)
        break
    except (ValueError, ZeroDivisionError):
        pass

if fuel >= 99:
    print("F")
elif fuel <= 1:
    print("E")
else:
    print(f"{fuel}%")

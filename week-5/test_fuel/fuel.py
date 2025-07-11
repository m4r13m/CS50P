def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            fuel = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(fuel))

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y or x < 0 or y < 0:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    return round(x/ y * 100)


def gauge(percentage):
    if percentage >= 99:
        return ("F")
    elif percentage <= 1:
        return ("E")
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()

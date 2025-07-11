def main():
    time = input("What time is it?")
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")


def convert(time):
    hour, minutes = time.split(":")
    minutes = float(minutes) / 60
    return float(hour) + minutes


if __name__ == "__main__":
    main()

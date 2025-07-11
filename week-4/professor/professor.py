from random import randint

def main():
    l = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(l)
        y = generate_integer(l)
        z = int(input(f"{x} + {y} = "))
        if z == x + y:
            score += 1
            continue
        else:
            print("EEE")
            for i in range(2):
                z = int(input(f"{x} + {y} = "))
                if z == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            print(f"{x} + {y} = {x+y}")
    print(score)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1,2,3]:
                continue
            return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    else:
        return randint(100,999)


if __name__ == "__main__":
    main()

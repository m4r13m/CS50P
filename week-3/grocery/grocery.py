grocery = {}
while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1

    except EOFError:
        break
for i in sorted(grocery):
    print(f"{grocery[i]} {i}")

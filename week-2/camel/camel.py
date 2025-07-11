word = input("camelCase: ")
for char in word:
    if char.isupper():
        word = word.replace(char, f"_{char}")
print(f"snake_case: {word.lower()}")

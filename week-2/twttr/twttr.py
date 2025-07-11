phrase = input("Input: ")
for character in phrase:
    if character in ["A", "E", "I", "U", "O", "a", "e", "i", "u", "o"]:
        phrase = phrase.replace(character, "")
print(f"Output: {phrase}")

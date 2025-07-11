def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    for char in word:
        if char in ["A", "a", "E", "e", "I", "i", "U", "u", "O", "o"]:
            word = word.replace(char, "")
    return word

if __name__ == "__main__":
    main()

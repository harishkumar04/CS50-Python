def main():
    text = input("Input: ")
    vowels = "aeiouAEIOU"
    result = ""

    for char in text:
        if char not in vowels:
            result += char

    print("Output:", result)


if __name__ == "__main__":
    main()

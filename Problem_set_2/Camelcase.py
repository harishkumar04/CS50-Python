def main():
    camelcase = input("Camelcase: ")
    snake_case = ""

    for char in camelcase:
        if char.isupper():
            snake_case += "_"+ char.lower()
        else:
            snake_case += char

    print("snake_case:",snake_case)

if __name__ == "__main__":
    main()
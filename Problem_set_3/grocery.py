def main():
    groceries = {}

    while True:
        try:
            item = input().strip().lower()
            if item:
                groceries[item] = groceries.get(item,0)+1
        except EOFError:
            print()
            break

    for item in sorted(groceries.keys()):
        print(f"{groceries[item]} {item.upper()}")

if __name__ == "__main__":
    main()

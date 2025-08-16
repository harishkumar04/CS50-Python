def main():
    due = 50

    while due > 0:
        print("Amount Due:", due)
        coin = int(input("Insert coin: "))
        
        if coin == 25 or coin == 10 or coin == 5:
            due -= coin
        else:
            continue

    print("Change Owed:", -due)


if __name__ == "__main__":
    main()

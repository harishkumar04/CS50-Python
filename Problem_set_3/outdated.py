def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]

    while True:
        date = input("Date: ").strip()

        try:
            if "/" in date:
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)
            elif "," in date:
                month_name, day, year = date.replace(",", "").split()
                month = months.index(month_name) + 1
                day, year = int(day), int(year)
            else:
                raise ValueError

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break

        except (ValueError, IndexError):
            continue


if __name__ == "__main__":
    main()
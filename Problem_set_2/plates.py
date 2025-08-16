def main():
    plate = input("PLATE:")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if not 2 <= len(s) <=6:
        return False

    if s[0].isdigit() or s[1].isdigit():
        return False

    if not s.isalnum():
        return False

    for i,ch in enumerate(s):
        if ch.isdigit():
            if ch == '0' and i==2 :
                return False
            if not s[i:].isdigit():
                return False
            break
    return True

if __name__ == "__main__":
    main()
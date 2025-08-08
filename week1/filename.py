x = input("File Name: ").strip().lower()
x = x.split(".")[-1] if '.' in x else ' '

match x :
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")


'''
# Another way to do this by using the function endswith() which then we can use it in a if statement like ".gif"
'''
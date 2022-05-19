ext = input("Provide a file name including the extension. ")


if ext.endswith(".gif"):
    print("image/gif")
elif ext.endswith(".png"):
    print("image/png")
elif ext.endswith(".jpg"):
    print("image/jpg")
elif ext.endswith(".jpeg"):
    print("image/jpeg")
elif ext.endswith(".pdf"):
    print("application/pdf")
elif ext.endswith(".txt"):
    print("text/plain")
elif ext.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
greeting = input("Type a greeting ")

if greeting.lower().startswith("hello"):
    print("$0")
elif greeting.lower().startswith("h"):
    print("$20")
else:
    print("$100")
vowels = ["A","E","I","O","U"]

msg = input("Type your twitter message: ")
twttrmsg = ""

for c in msg:
    if not c.upper() in vowels:
        twttrmsg += c

print(twttrmsg)
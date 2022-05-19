answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

try:
    num_answer = int(answer)
except:
    num_answer = 0
if num_answer == 42 or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
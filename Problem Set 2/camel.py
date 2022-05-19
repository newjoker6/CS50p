camelCase = input("Give a variable in camelCase. ")
snake_case = ""

for c in camelCase:
    if c == c.upper():
        snake_case += "_"
        snake_case += c
    else:
        snake_case += c

print(snake_case)


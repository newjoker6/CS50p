Expression = input("Math Expression ")

expression_split = Expression.split(" ")

x = float(expression_split[0])
y = expression_split[1]
z = float(expression_split[2])
answer: float

if y == "+":
    answer = x + z

elif y =="-":
    answer = x - z

elif y == "*":
    answer = x * z

elif y == "/":
    answer = x / z

print(answer)

text = input('How much fuel is left in the car? x/y\n')

try:
    x = int(text[0])
    y = int(text[2])
    if x <= y:
        value = (x/y) * 100
        print(f'{value}%')
    else:
        print('x can not be larger than y.')

except (ValueError, ZeroDivisionError):
    print('try again')
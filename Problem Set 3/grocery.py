list = {}

while True:
    try:
        item = input()
        if not item in list.keys():
            list[f'{item}'] = 1
        else:
            list[f'{item}'] += 1

    except EOFError:
        sorted_list = sorted(list.keys())
        for i in sorted_list:
            num = list[i]
            print(f'{num} {i}')
        break
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    Date = input('Date: ')
    if '/' in Date:
        Date = Date.split('/')
    elif ' ' in Date:
        Date = Date.split(' ')

    print(int(Date[0])-1)
    print(len(months))
    try:
        if Date[0] in months or int(Date[0]) <= len(months):
            print(f'{Date[2]}-{Date[0]}-{Date[1]}')
        elif int(Date[0]) <= len(months):
            print(f'{Date[2]}-{Date[0]}-{Date[1]}')
        break
    except:
        print('try again')
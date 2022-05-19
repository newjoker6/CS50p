InsertedAmount = 0
AmountDue = 50

def calculate_change():
    change = InsertedAmount - 50
    print(f"Change Owed: {change}")


while InsertedAmount < 50:
    print(f"Amount Due: {AmountDue}")
    insert = input("Insert Coins: ")
    InsertedAmount += int(insert)
    AmountDue -= int(insert)
    print(f"Inserted: {InsertedAmount}")

calculate_change()
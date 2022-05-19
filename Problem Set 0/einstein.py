mass = input("enter the weight of a mass in kg ")
mass = int(mass)

def calculate_joules(m):
    c = 300000000
    e = m * c**2
    print("The energy of this mass is " + str(e))

calculate_joules(mass)
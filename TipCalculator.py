# Tip Calculator

def person_pay(a, b):
    each_person_pays = a / b  # Calculates the amount of $ each person should pay
    return each_person_pays


def tip_payment(a, b):
    if b == 0:
        each_person_tips = 0
    else:
        each_person_tips = a * (b / 100)  # Calculates the amount of $ each person should tip
    return each_person_tips


print ("How much is the bill in US Dollars?")
while True:
    try:
        bill = float(raw_input("$"))
        break
    except:
        print ("Must be number value")

print ("How many people ?")
while True:
    try:
        people = float(raw_input())
        break
    except:
        print ("Must be number value")
print ("What percentage of tip ?")
while True:
    try:
        tip = float(raw_input("%"))
        break
    except:
        print ("Must be number value")
each_pays = person_pay(bill, people)
each_tips = tip_payment(each_pays, tip)
print ("calculating Payment...")
print ("Each person pays ${0:.2f} for the bill".format(each_pays))
print ("Each person pays ${0:.2f} for the tip".format(each_tips))
print ("Which means each person will pay a total of ${0:.2f}".format(each_pays + each_tips))

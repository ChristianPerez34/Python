# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
def divider(number, checker):
    if (number % checker == 0):
        print("{} divides evenly into {}".format(checker,num))
    else:
        print("{} does not divide evenly into {}".format(checker,num))


num = int(input("Input a number: "))
check = int(input("Input a checker: "))
divider(num,check)
if(num % 4 == 0):
    print("{} is a multiple of 4, therefore it is even".format(num))
elif(num % 2 == 0):
    print("{} is even".format(num))
else:
    print("{} is odd".format(num))

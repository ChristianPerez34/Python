# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime

name = raw_input("What is your name? ")
age = input("How old are you? ")
times = input("How many time should message be shown? ")
if(age < 100):
    years = 100 - int(age)
    thisYear = datetime.datetime.now()
    years += int(thisYear.year)
    for i in range(times):
        print("{}, you will turn 100 in {}".format(name,years))
else:
    print("You are already over 100 years old")
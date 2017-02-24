# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

print("Input number to be generated into a list seperated by spaces: ")
a = [int(x) for x in raw_input().split()]
b = []
limit = int(input("Input limiting number: "))
for i in a:
    if(i < limit):
        b.append(i)
b.sort()
print(b)
num = int(input("Fill in a number => "))
list = []

for x in range (2, num+1):
    if (num % x) == 0:
        list.append(x)

print (list)

## https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
## One line? 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

num = int(input("Fill in a number => "))
for x in a:
    if (x < num):
        print (x)


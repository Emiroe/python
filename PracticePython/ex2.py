## https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html\

number = int(input("Fill in a number => "))
check = int(input("What number should we check against this? => "))

if (number % 4) == 0 and (number % check) == 0:
    print ("This number can be multiplied by 4 and can be divided by %d." % (check, ))
elif (number %4) == 0 and (number % check) != 0:
    print ("This number can be multiplied by 4 but can not be divided by %d." % (check, ))
elif (number % 2) == 0 and (number % check) == 0:
    print ("This is an even number and can be divided by %d." % (check, ))
elif (number % 2) == 0 and (number % check) != 0:
    print ("This is an even number but can not be divided by %d." % (check, ))
elif (number % check) == 0:
    print ("This is an uneven number and can be be divided by %d." % (check, ))
else:
    print ("This is an uneven number but can not be divided by %d." % (check, ))
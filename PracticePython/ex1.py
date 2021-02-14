### https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime

currentdate = datetime.datetime.now()


name = input("What is your name? => ")
age = int(input("What is your age? => ")) ## Ask for input as a integer instead of a string.
copies = int(input("How many copies do you want to print? =>" ))
hundred = 100 - age
currentdate = datetime.datetime.now()
currentyear =(currentdate.year)
futureyear = currentyear + hundred 

message_intro = ("Hi %s, you are currently %d years old." % (name, age,))
message_calc = ("It is still %d years until you are 100 years old." % (hundred, )) 
message_year = ("It will be the year %d. \n" % (futureyear, ))

for i in range(copies):
    print (message_intro)
    print (message_calc)
    print (message_year)

#print ("Hi %s, you are currently %d years old." % (name, age,))
#print ("It is still %d years until you are 100 years old. \n" % hundred, ) 
## https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

string = input("Check this string => ")
reverse_string = string[::-1]

if reverse_string == string:
    print ("This is a palindrome.")
else:
    print ("This is a regular word.")

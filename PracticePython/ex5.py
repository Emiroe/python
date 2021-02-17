## https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

import random

a = random.sample(range(1,100), 20)
b = random.sample(range(1,100), 30)
c = [ ]

for x in a:
    if x in b:
        if x not in c:
            c.append(x)
print (a)
print (b)
print (c)
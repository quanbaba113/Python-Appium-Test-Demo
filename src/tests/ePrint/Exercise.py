from random import randint
number = randint(1,9)
if number % 2 == 0:
    raise NameError("%d is even" %number)
else:
    raise NameError("%d is odd " % number)
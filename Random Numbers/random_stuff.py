from random import randint
from random import shuffle
from random import seed
import sys
from random import randrange

# https://pynative.com/python-random-seed/#h-get-a-seed-value-used-by-a-random-generator

counter = 0
random_lst = []

while counter < 10:

    x = randint(0,20)
    random_lst.append(x)
    counter += 1



print(random_lst)
print(random_lst)
print(random_lst)

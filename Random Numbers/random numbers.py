from random import seed
from random import randint

seed(1)
value_list = []
counter = 0
while counter < 10:
    value = randint(0, 10)
    value_list.append(value)
    counter += 1
print(value_list)




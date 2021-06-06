import random
import pandas as pd

# print(random_list)
# random.shuffle(random_list)
# print(random_list)
# random.shuffle(random_list)
# print(random_list)
i = 10
j = 30
combo_lst = []
counter = 0
while counter < 4:
    random_list = random.sample(range(i, j), 10)
    random.shuffle(random_list)
    counter += 1
    print(random_list)
    combo_lst.append(random_list)
print(combo_lst)
df = pd.DataFrame(combo_lst)
print(df)


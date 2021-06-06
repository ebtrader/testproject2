from random import seed
from random import randint
import pandas as pd

# https://www.kite.com/python/answers/how-to-append-a-list-as-a-row-to-a-pandas-dataframe-in-python
# https://www.kite.com/python/answers/how-to-convert-a-list-of-lists-into-a-pandas-dataframe-in-python
# https://www.geeksforgeeks.org/create-a-pandas-dataframe-from-lists/

class Random_generator:

    def gen_random(self):
        i = 1
        seed(i)
        value_list = []
        lst_of_lst = []
        counter = 0
        counter_lst = 0
        while counter_lst < 4:

            while counter < 10:
                value = randint(0, 10)
                value_list.append(value)
                counter += 1
            lst_of_lst.append(value_list)
            counter_lst += 1

        print(lst_of_lst)
        # print(value_list)

def main():
    app = Random_generator()
    app.gen_random()


if __name__ == "__main__":
    main()



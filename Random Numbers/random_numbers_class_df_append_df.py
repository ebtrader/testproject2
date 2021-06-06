from random import seed
from random import randint
from random import shuffle
from random import sample
import pandas as pd

# https://www.kite.com/python/answers/how-to-append-a-list-as-a-row-to-a-pandas-dataframe-in-python
# https://www.kite.com/python/answers/how-to-convert-a-list-of-lists-into-a-pandas-dataframe-in-python
# https://www.geeksforgeeks.org/create-a-pandas-dataframe-from-lists/
# https://www.tutorialspoint.com/generating-random-number-list-in-python

class Random_generator:

    def gen_random(self):
        value_list = []
        lst_of_lst = []
        counter = 0
        counter_lst = 0
        start = 0
        end = 10
        while counter_lst < 4:
            while counter < 10:
                value = randint(start, end)
                value_list.append(value)
                counter += 1
                

            lst_of_lst.append(value_list)
            counter_lst += 1

        print(lst_of_lst)
        df = pd.DataFrame(lst_of_lst)
        print(df)

def main():
    app = Random_generator()
    app.gen_random()


if __name__ == "__main__":
    main()



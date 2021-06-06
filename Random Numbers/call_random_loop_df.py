import time

from random_numbers_class import Random_generator
import pandas as pd

# https://www.kite.com/python/answers/how-to-append-a-list-as-a-row-to-a-pandas-dataframe-in-python
# https://www.kite.com/python/answers/how-to-convert-a-list-of-lists-into-a-pandas-dataframe-in-python


class CallRandomLoop:
    def third_try(self):
        counter1 = 0
        n = 1

        while counter1 < 4:
            Random_generator.gen_random(self, n)
            n = counter1
            counter1 += 1



def main():
    app = CallRandomLoop()
    app.third_try()


if __name__ == "__main__":
    main()
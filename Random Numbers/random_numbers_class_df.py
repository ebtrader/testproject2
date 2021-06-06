from random import seed
from random import randint
import pandas as pd

class Random_generator:

    def gen_random(self, i=1):
        seed(i)
        value_list = []
        counter = 0
        while counter < 10:
            value = randint(0, 10)
            value_list.append(value)
            counter += 1
        df = pd.DataFrame(value_list, columns=['Random'])

        print(value_list)
        print(df)

def main():
    app = Random_generator()
    app.gen_random()


if __name__ == "__main__":
    main()



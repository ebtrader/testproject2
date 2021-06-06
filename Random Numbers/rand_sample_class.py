import random
import pandas as pd

# print(random_list)
# random.shuffle(random_list)
# print(random_list)
# random.shuffle(random_list)
# print(random_list)

class MessUp:
    def do_the_mix(self):
        i = 10
        j = 30
        combo_lst = []
        counter = 0
        num_of_rows = 4
        while counter < num_of_rows:
            random_list = random.sample(range(i, j), 10)
            random.shuffle(random_list)
            counter += 1
            print(random_list)
            combo_lst.append(random_list)
        print(combo_lst)
        df = pd.DataFrame(combo_lst)
        print(df)

def main():
    app = MessUp()
    app.do_the_mix()

if __name__ == "__main__":
    main()


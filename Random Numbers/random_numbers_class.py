from random import seed
from random import randint

class Random_generator:

    def gen_random(self):
        seed(1)
        value_list = []
        counter = 0
        while counter < 10:
            value = randint(0, 10)
            value_list.append(value)
            counter += 1
        print(value_list)

def main():
    app = Random_generator()
    app.gen_random()


if __name__ == "__main__":
    main()



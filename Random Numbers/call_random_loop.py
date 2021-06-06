from random_numbers_class import Random_generator

class CallRandomLoop:
    def third_try(self):
        counter1 = 0
        n = 3
        while counter1 < 6:
            Random_generator.gen_random(self, n)
            n = counter1+1
            counter1 += 1

def main():
    app = CallRandomLoop()
    app.third_try()


if __name__ == "__main__":
    main()
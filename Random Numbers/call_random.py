from random_numbers_class import Random_generator

class CallSomeRandom:
    def third_try(self):
        Random_generator.gen_random(self)

def main():
    app = CallSomeRandom()
    app.third_try()


if __name__ == "__main__":
    main()



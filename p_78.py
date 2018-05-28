import random, sys

if __name__ == '__main__':

    some = 0

    for i in range(5):
        some = random.randint(1, 10)
        if some < 5:
            print('EXIT')
            sys.exit()
        else:
            print(some)

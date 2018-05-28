def some_function(some_int):
    try:
        return 2 / some_int
    except ZeroDivisionError:
        print('Error : ..')


if __name__ == '__main__':
    print(some_function(11))
    print(some_function(0))

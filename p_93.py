def some_function():
    global eggs
    eggs = 'aa'
    print(eggs)


if __name__ == '__main__':
    # some_function 이 호출되어서 eggs가 정의되어야하는 데 되어있지 않다.
    # print(eggs)

    some_function()
    print(eggs)


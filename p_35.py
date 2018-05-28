if __name__ == '__main__':
    # 자바스크립트와 자바, 스칼라와 달리 합쳐지지 않는다.
    # print('Alice' + 42)

    # 파이썬에서는 기본적으로 스네이크 표기법을 기본으로 채택하고 있다.
    some_int = 42
    some_str = 'Alice'

    # 아래도 안됨.
    # print(some_int+some_str)

    # 이런식으로 하면 된다.
    print('Alice' + str(42))

    # 하지만 이런게 된다. -_-;;
    # > AlticeAliceAliceAliceAlice
    print('Alice' * 5)

    print(len('Alice' * 5))

    print(int('42'))

    some = 2 > 3
    some2 = 2 == 2

    a1 = 'hi'

    a2 = 'hi'

    a3 = 'HI'

    print(some)
    print(some2)

    print(a1 == a2)
    print(a1 == a3)

    # 이진 연산자
    # > true and false  => false 로 리턴된다.
    print(a1 == a2 and a1 == a3)

    # > true or false => true 로 리턴
    print(a1 == a2 or a1 == a3)

    if a1 == 'hi2':
        print('Wow')

    elif a1 == 'hi1':
        print('Wow22')
    else:
        print('Shit')

    # 아래 a2 도 참이지만, 선 a1 비교문에서 true가 반환되기에 무시(skip) 된다.
    if a1 == 'hi':
        print('a1')
    elif a2 == 'hi':
        print('a2')
    else:
        print('Not Wrong..')

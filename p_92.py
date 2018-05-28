ss = 'Hello'

def spam():
    # 쇼킹하군 미친거 같다. 이러면 언제든 값의 오염 즉, 사이드이팩트가 일어날수있다.
    global eggs
    eggs = 'spam'
    print(eggs)
    print(ss)


if __name__ == '__main__':
    eggs = 'global'
    spam()
    print(eggs)
    print(ss)
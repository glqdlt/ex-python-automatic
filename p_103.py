if __name__ == '__main__':
    spam = ['cat', 'bat', 'rat', 'elephant']
    for s in spam:
        print(s)

    print('====')
    print(spam[-1])
    print(spam[1])
    print(spam[1:3])
    print(spam[0:-1])
    print(spam[1:])
    print(spam[:2])
    print('====')
    two_wat = [['dog', 'dog2'], ['wolf', 'wolf2']]
    print(two_wat[0][0])
    print(two_wat[1][1])

    print([1, 2, 3] + ['x', 'y'])
    print(two_wat)
    print(two_wat[0] + two_wat[1])
    del two_wat[1]
    print(two_wat)

    for i in range(len(spam)):
        print(i)

    print('cat' in spam)
    print('cat2' in spam)
    print('cat2' not in spam)

if __name__ == '__main__':
    spam = ['hello', 'hi', 'howby']
    print(spam.index('hi'))
    spam.append('wow')
    print(spam)
    spam.insert(1, 'chicken')
    print(spam)
    del spam[1]
    print(spam)
    spam.remove('wow')
    spam.insert(1, 'zz')
    print(spam)
    spam.sort()
    print(spam)

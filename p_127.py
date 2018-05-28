import copy

if __name__ == '__main__':
    spam = ['A', 'B', 'C']
    spam_in_array = ['a', 'b', 'c', [1, 2, 3]]

    cheese = copy.copy(spam)

    print(spam)
    print(cheese)
    print()

    cheese[1] = 42
    print(spam)
    print(cheese)

    cheese_in_array = copy.copy(spam_in_array)
    cheese_in_array_deep = copy.deepcopy(spam_in_array)
    print(spam_in_array)
    # copy로 할 경우 spam_in_array 안의 [1,2,3] 리스트를 레퍼런스 참조만 copy 한다.
    print(cheese_in_array)
    print(cheese_in_array_deep)

    # copy로 복사했을 경우 사실상 레퍼런스 참조만 된 것이기 때문에.. spam_in_array의 변경에도 영향을 받는다.
    spam_in_array[3][0] = 2
    print()

    print(spam_in_array)
    print(cheese_in_array)
    # deep_copy의 경우 리스트 객체안의 값 자체를 deep_copy 해버렸으므로 변경되지않는다.
    print(cheese_in_array_deep)

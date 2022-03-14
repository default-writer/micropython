from itertools import takewhile, dropwhile

def sum78(nums):
    i = enumerate(nums)
    return sum([x[1] for x in takewhile(lambda x: x[1]!=7, i)]+[x[1] for x in dropwhile(lambda x: x[1]!=8, i)][1:])

def test_sum78():
    assert sum78([1, 2, 2]) == 5
    assert sum78([1, 2, 2, 7, 99, 99, 8]) == 5
    assert sum78([1, 1, 7, 8, 2]) == 4
    assert sum78([1, 1, 7, 2022, 8, 2]) == 4

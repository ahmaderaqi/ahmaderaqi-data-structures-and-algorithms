from binary_serch import binary_search
def test_one():
    arr=[0,1,2,3,4,5,6,7,8]
    expected = 2
    actual = binary_search(arr,2)
    assert expected == actual

def test_two():
    arr=[0,13,4,5,6,7,8]
    expected = -1
    actual = binary_search(arr,2)
    assert expected == actual

def test_three():
    arr=[0,1,2,3]
    expected = 2
    actual = binary_search(arr,2)
    assert expected == actual


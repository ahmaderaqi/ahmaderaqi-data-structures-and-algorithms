from code_challenges.sort.insertion.insertion_sort import insertion_sort

def test_one():
    arr1=[8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]
    actual = insertion_sort(arr1)
    assert expected == actual

def test_two():
    arr1=[20,18,12,8,5,-2]
    expected = [-2, 5, 8, 12, 18, 20]
    actual = insertion_sort(arr1)
    assert expected == actual

def test_three():
    arr1=[5,12,7,5,5,7]
    expected = [5, 5, 5, 7, 7, 12]
    actual = insertion_sort(arr1)
    assert expected == actual

def test_four():
    arr1=[2,3,5,7,13,11]
    expected = [2, 3, 5, 7, 11, 13]
    actual = insertion_sort(arr1)
    assert expected == actual
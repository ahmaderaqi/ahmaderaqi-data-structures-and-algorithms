from code_challenges.stack_and_queue.stack_queue_brackets_CC13_folder.stack_queue_brackets_file import validate_brackets_2
from code_challenges.stack_and_queue.stack_queue_brackets_CC13_folder.stack_queue_brackets_file import validate_brackets


def test_1():
    arr1="(ahmad[)]"
    expected = True
    actual = validate_brackets_2(arr1)
    assert expected == actual

def test_empty():
    arr1="ahmad"
    expected = True
    actual = validate_brackets_2(arr1)
    assert expected == actual

def test_2():
    arr1="(ahmad[){]"
    expected = False
    actual = validate_brackets_2(arr1)
    assert expected == actual

def test_3():
    arr1="(ah}mad[)]"
    expected = False
    actual = validate_brackets_2(arr1)
    assert expected == actual


# tests for way 1

def test_4():
    arr1="(ah}m{ad[)}}{{]"
    expected = True
    actual = validate_brackets(arr1)
    assert expected == actual

def test_5():
    arr1="(ahmad[)]"
    expected = True
    actual = validate_brackets(arr1)
    assert expected == actual

def test_empty2():
    arr1="ahmad"
    expected = True
    actual = validate_brackets(arr1)
    assert expected == actual

def test_6():
    arr1="(ahmad[){]"
    expected = False
    actual = validate_brackets(arr1)
    assert expected == actual


def test_7():
    arr1="(ah}mad[)]"
    expected = False
    actual = validate_brackets(arr1)
    assert expected == actual

def test_8():
    arr1="(ah}m{ad[)}}{{]"
    expected = True
    actual = validate_brackets(arr1)
    assert expected == actual
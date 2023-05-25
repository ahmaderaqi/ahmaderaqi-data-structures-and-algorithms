from code_challenges.insert_shift_array.insert_shift_array import insertShiftArray
import pytest

def test_one():
    arr1=[1,2,3,4,5,7]
    expected = [1,2,3,10,4,5,7]
    actual = insertShiftArray(arr1,10)
    assert expected == actual

def test_two():
    arr2=[1,2]
    expected = [1,5,2]
    actual = insertShiftArray(arr2,5)
    assert expected == actual

def test_three():
    arr3=[1]
    expected = [1,10]
    actual = insertShiftArray(arr3,10)
    assert expected == actual

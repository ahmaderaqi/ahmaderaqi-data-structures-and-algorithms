from code_challenges.stack_and_queue.stack_queue_brackets_CC13_folder.stack_queue_brackets_file import is_balanced_parenthesis
from code_challenges.stack_and_queue.stack_queue_brackets_CC13_folder.stack_queue_brackets_file import validate_brackets


def test_is_balanced_parenthesis_balanced():
    assert is_balanced_parenthesis("()") == True
    assert is_balanced_parenthesis("()()") == True
    assert is_balanced_parenthesis("(())") == True
    assert is_balanced_parenthesis("((()))") == True
    assert is_balanced_parenthesis("()()()") == True
    assert is_balanced_parenthesis("()(())") == True

def test_is_balanced_parenthesis_unbalanced():
    assert is_balanced_parenthesis("(") == False
    assert is_balanced_parenthesis(")") == False
    assert is_balanced_parenthesis(")(") == False
    assert is_balanced_parenthesis("()(") == False
    assert is_balanced_parenthesis(")()(") == False

def test_is_balanced_parenthesis_empty():
    assert is_balanced_parenthesis("") == True

def test_is_balanced_parenthesis_nested():
    assert is_balanced_parenthesis("((())())") == True
    assert is_balanced_parenthesis("((()())") == False
    assert is_balanced_parenthesis("(((())))") == True
    assert is_balanced_parenthesis("()((())())") == True

def test_is_balanced_parenthesis_other_characters():
    assert is_balanced_parenthesis("(abc(def)xyz)") == True
    assert is_balanced_parenthesis("(abc(def)xyz") == False
    assert is_balanced_parenthesis("abc(def)xyz") == True
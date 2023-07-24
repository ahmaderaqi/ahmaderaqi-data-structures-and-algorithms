import pytest

from code_challenges.hash_table.repeated_word_hash.repeated import repeated_word

def test_repeated_word():
    sentence1 = "Hello I'm ahmad iraqi. iraqi is my family name."
    assert repeated_word(sentence1) == "iraqi"

    sentence2 = "My name is ahmad zaher."
    assert repeated_word(sentence2) is None

    sentence3 = ""
    assert repeated_word(sentence3) is None

    sentence4 = "ahmad! ahmad! Zaher iraqi"
    assert repeated_word(sentence4) == "testing!"

    sentence5 = "123 000 789 123 09"
    assert repeated_word(sentence5) == "123"

    sentence6 = "Hello, hello! How are you"
    assert repeated_word(sentence6) == "hello"

    sentence7 = "Hello, HELLO, hello"
    assert repeated_word(sentence7) == "hello"

if __name__ == "__main__":
    pytest.main()

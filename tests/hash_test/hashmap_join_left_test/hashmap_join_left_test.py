from code_challenges.hash_table.hashmap_left_join.hashmap_left_join import left_join  
import pytest
def test_left_join():
    synonyms = {
        "happy": "joyful",
        "sad": "unhappy",
        "good": "excellent",
        "bad": "terrible"
    }

    antonyms = {
        "good": "bad",
        "happy": "sad",
        "strong": "weak"
    }

    output = left_join(synonyms, antonyms)
    assert isinstance(output, list)
    assert all(isinstance(row, tuple) for row in output)

    assert len(output) == len(synonyms)

    assert ('happy', 'joyful', 'sad') in output
    assert ('sad', 'unhappy', None) in output
    assert ('good', 'excellent', 'bad') in output
    assert ('bad', 'terrible', None) in output
    assert ('strong', None, 'weak') not in output  


if __name__ == "__main__":
    pytest.main()

import pytest
from hashtable import HashTable

def test_hashtable():
    hash_table = HashTable()

    hash_table.set("key1", "value1")
    hash_table.set("key2", "value2")
    hash_table.set("key3", "value3")

    assert hash_table.get("key2") == "value2"

    assert hash_table.has("key3") is True
    assert hash_table.has("key4") is False

    assert hash_table.keys() == ["key1", "key2", "key3"]

    assert hash_table.hash("key1") == hash_table.custom_hash("key1")


def test_hashtable_collision():
    hash_table = HashTable(size=2)

    hash_table.set("key1", "value1")
    hash_table.set("key2", "value2")
    hash_table.set("key3", "value3")

    assert hash_table.get("key2") == "value2"
    assert hash_table.get("key3") == "value3"

    assert hash_table.has("key1") is True
    assert hash_table.has("key2") is True
    assert hash_table.has("key3") is True
    assert hash_table.has("key4") is False

    assert hash_table.keys() == ["key1", "key2", "key3"]


if __name__ == "__main__":
    pytest.main()

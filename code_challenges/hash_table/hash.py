from linked_list import LinkedList

class HashTable():
    def __init__(self, size=3):
        self.size = size
        self.map = [None] * size

    def custom_hash(self, key):
        sum_of_ascii = 0
        for ch in key:
            ascii_of_ch = ord(ch)
            sum_of_ascii += ascii_of_ch
        temp = sum_of_ascii * 599
        index = temp % self.size
        return index

    def set(self, key, value):
        hashed_key = self.custom_hash(key)
        if not self.map[hashed_key]:  # If the bucket is empty
            self.map[hashed_key] = [key, value]
        else:  # Collision happened
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key, value])
            else:  # If the bucket contains one pair only
                chain = LinkedList()
                existing_pair = self.map[hashed_key]
                new_pair = [key, value]
                self.map[hashed_key] = chain
                chain.add(existing_pair)
                chain.add(new_pair)

    def get(self, key):
        hashed_key = self.custom_hash(key)
        if isinstance(self.map[hashed_key], LinkedList):
            curr = self.map[hashed_key].head
            while curr:
                if curr.value[0] == key:
                    return curr.value[1]
                curr = curr.next
        elif self.map[hashed_key] and self.map[hashed_key][0] == key:
            return self.map[hashed_key][1]
        raise KeyError(f"Key '{key}' does not exist in the table.")

    def has(self, key):
        hashed_key = self.custom_hash(key)
        if isinstance(self.map[hashed_key], LinkedList):
            curr = self.map[hashed_key].head
            while curr:
                if curr.value[0] == key:
                    return True
                curr = curr.next
        elif self.map[hashed_key] and self.map[hashed_key][0] == key:
            return True
        return False

    def keys(self):
        keys = []
        for bucket in self.map:
            if isinstance(bucket, LinkedList):
                curr = bucket.head
                while curr:
                    keys.append(curr.value[0])
                    curr = curr.next
            elif bucket:
                keys.append(bucket[0])
        return keys

    def hash(self, key):
        return self.custom_hash(key)

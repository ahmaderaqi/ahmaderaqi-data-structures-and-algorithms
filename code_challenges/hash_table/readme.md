# hash table 
A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found
## Whiteboard Process




## Approach & Efficiency
reverse an array without useing any bilt-in functions

## Algorithm


1. `custom_hash(key)`: This method calculates the hash value for a given key by iterating over each character in the key, calculating the ASCII value for each character, and summing them up. It then applies a multiplication and modulo operation to ensure the resulting index is within the range of the hashtable size. The algorithm can be summarized as follows:
   - Initialize `sum_of_ascii` to 0.
   - Iterate over each character `ch` in the key.
     - Calculate the ASCII value of `ch` and add it to `sum_of_ascii`.
   - Calculate `temp` as `sum_of_ascii * 599`.
   - Calculate `index` as `temp % self.size`.
   - Return `index`.

2. `set(key, value)`: This method sets a key-value pair in the hashtable. The algorithm is as follows:
   - Calculate the hash value (`hashed_key`) for the given key using the `custom_hash` method.
   - If the bucket at `hashed_key` is empty:
     - Create a new entry with the key-value pair and assign it to the bucket.
   - Otherwise, if the bucket contains a linked list:
     - Traverse the linked list and check if the key already exists.
     - If the key exists, update its value with the new value.
     - If the key doesn't exist, append a new node with the key-value pair at the end of the linked list.
   - Otherwise, if the bucket contains a single key-value pair:
     - Create a new linked list.
     - Move the existing pair to the linked list.
     - Append a new node with the key-value pair at the end of the linked list.
     - Assign the linked list to the bucket.

3. `get(key)`: This method retrieves the value associated with a given key from the hashtable. The algorithm is as follows:
   - Calculate the hash value (`hashed_key`) for the given key using the `custom_hash` method.
   - If the bucket at `hashed_key` is a linked list:
     - Traverse the linked list and check if the key matches any node's key.
     - If a match is found, return the corresponding value.
   - Otherwise, if the bucket is a single key-value pair:
     - Check if the key of the pair matches the given key.
     - If it does, return the corresponding value.
   - If no match is found, raise a `KeyError` indicating that the key doesn't exist in the table.

4. `has(key)`: This method checks if a key exists in the hashtable. The algorithm is as follows:
   - Calculate the hash value (`hashed_key`) for the given key using the `custom_hash` method.
   - If the bucket at `hashed_key` is a linked list:
     - Traverse the linked list and check if the key matches any node's key.
     - If a match is found, return `True`.
   - Otherwise, if the bucket is a single key-value pair:
     - Check if the key of the pair matches the given key.
     - If it does, return `True`.
   - If no match is found, return `False`.

5. `keys()`: This method returns a collection of all keys in the hashtable. The algorithm is as follows:
   - Initialize an empty list `keys`.
   - Iterate over each bucket in the hashtable.
     - If the bucket is a linked list:
       - Traverse the linked list and add each node's key to `keys`.
     - Otherwise, if the bucket is a single key-value pair:
       - Add the key of the pair to `keys`.
  
## Big O
### 1. custom_hash
time complexity is O(N)
space complexity is O(1)

### 2. set
time complexity is O(1)
space complexity is O(1)

### 3. get
time complexity is O()
space complexity is O(1)

### 4. has
time complexity is O(1)
space complexity is O(1)

### 5. keys
time complexity is O(N)
space complexity is O(1)

### 6. hash
time complexity is O(N)
space complexity is O(1)
## Solution
|Code challenge1  |    [code1](./hash.py)
|Code challenge1  |    [code1](./linked_list.py)


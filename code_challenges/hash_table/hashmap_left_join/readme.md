# hashmap left 
Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.

    LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
    If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.)




## Approach & Efficiency
Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.

## Algorithm

1. Initialize an empty list called `result` to hold the output of the LEFT JOIN operation.

2. Iterate through the keys and values of the `synonyms` hashmap.
   - For each key-value pair (word and synonym), check if the word exists as a key in the `antonyms` hashmap.

3. If the word exists in the `antonyms` hashmap, get its corresponding antonym value; otherwise, set the antonym to `None`.

4. Create a tuple with three elements: the word, its synonym, and its antonym (which may be `None`).

5. Append the tuple to the `result` list.

6. Continue iterating through all the keys and values in the `synonyms` hashmap.

7. Once the iteration is complete, the `result` list will contain the LEFT JOIN result, which combines the word, synonym, and antonym information, following the LEFT JOIN logic.


## Big O
time complexity is O(n)
space complexity is O(n)

## Solution
|Code challenge |    [code1](./hashmap_left_join.py)

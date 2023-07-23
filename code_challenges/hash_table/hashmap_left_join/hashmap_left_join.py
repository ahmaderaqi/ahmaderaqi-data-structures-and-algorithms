def left_join(synonyms, antonyms):
    """Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.

    LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
    If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row."""
    result = []

    for word, synonym in synonyms.items():
        antonym = antonyms.get(word, None)
        result.append((word, synonym, antonym))

    return result


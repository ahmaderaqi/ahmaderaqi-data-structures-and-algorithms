def repeated_word(string):
    """
    this function returns the first repeated word in a string by using hash table
    """
    words = string.lower().split()  
    counter = {}  
    for word in words:
        if word in counter:
            return word  
        else:
            counter[word] = 1

    return None  



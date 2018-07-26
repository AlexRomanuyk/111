def invert_hash(dictionary):
    inverted_dict = {}
    for a, b in dictionary.items():
        inverted_dict.update({b : a})
    return inverted_dict
    

def pig_latin(word):
    # Happy coding ;)
    if len(word) > 3 and word.isalpha():
        first = word[0]
        new_word = word[1:] + first + "ay"       
    return new_word 

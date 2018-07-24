def filter_list(l):
    list_of_ints = []
    for i in l:
        if type(i) is int:
            list_of_ints.append(i)
    return list_of_ints

def factorsRange(n, m):
    dict_of_factors = {}
    for i in range(n, m+1):
        value = []
        for b in range(2, i):
            if i % b == 0:
               value.append(b)
        if not value:
            value = ['None']
        dict_of_factors[i] = value
        value = []
    return dict_of_factors

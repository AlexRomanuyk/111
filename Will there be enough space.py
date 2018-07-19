def enough(cap, on, wait):
    # Your code here
    if on + wait <= cap: 
        return 0 
    return -1 * (cap - on - wait)

def makeMove(sticks):
    # Your code here ;)
    if sticks < 4:
        return sticks 
    if sticks % 4 == 0: 
        return 1
    return sticks % 4

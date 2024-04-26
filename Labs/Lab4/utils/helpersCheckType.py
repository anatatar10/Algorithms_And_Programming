def checkType(typeVector):
    if typeVector >= 1:
        if isinstance(typeVector, int) == True:
            return 1
        else:
            return 0
    else:
        return 0


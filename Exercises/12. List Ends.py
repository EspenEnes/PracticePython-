a = [5, 10, 15, 20, 25]

def getEnds(list):
    result = []
    result.append(list[0])
    result.append(list[-1])
    return result


print getEnds(a)
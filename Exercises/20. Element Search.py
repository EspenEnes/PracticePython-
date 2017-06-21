a = [7,9,15,98,101]


def InBetween(list, number):
    if list[0] < number and list[-1] > number:
        return True
    else:
        return False



print InBetween(a,5)

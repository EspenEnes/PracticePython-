a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]



Number = raw_input("give a number")


def ListLess(Number):          # Multi line List print
    b = []
    for x in a:
        if x < int(Number):
            b.append(x)
    print b
ListLess(Number)




print [x for x in a if x < int(Number)]  # one line List print
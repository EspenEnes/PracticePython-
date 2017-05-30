

def DiversorCheck():
    CheckList = range(1,int(raw_input("Give me a Number")) + 1)
    for x in CheckList:
        if max(CheckList) % x == 0:
            print str(max(CheckList)) + "/" + str(x) + "=" + str(max(CheckList)/x)


DiversorCheck()
import random
a = []
b = []

for x in range(0,random.randint(0,100)):
    a.append(random.randint(0,1000))

for x in range(0,random.randint(0,100)):
    b.append(random.randint(0,1000))







#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def overlap(x,y):
    masterlist =[]
    slavelist = []
    newlist = []
    if len(x) < len(y):
        masterlist = x
        slavelist = y
    else:
        masterlist = y
        slavelist = x

    for x in masterlist:
        if x in slavelist:
            if x not in newlist:
                newlist.append(x)
    print newlist

overlap(a,b)


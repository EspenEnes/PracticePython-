import random


def generateList(population,k):
    result = []
    for x in range(population):
        result.append(random.randrange(1,k))
    return result

list = generateList(7,31)
print "Original:" + str(list)



def remDuplicates(list,getdupset=False, getunikset=False):


    result = []
    result2 = []
    for number in list:
        if number not in result:
            result.append(number)
        else:
            result2.append(number)

    if getdupset == True:
        return result2
    if getunikset == True:
        result3 = []
        for number in result:
            if number not in result2:
                result3.append(number)
        return result3


    else:
        return result




print "Set: " + str(remDuplicates(list))
print "Removed: " + str(remDuplicates(list,getdupset=True))
print "Unik: " + str(remDuplicates(list,getunikset=True))

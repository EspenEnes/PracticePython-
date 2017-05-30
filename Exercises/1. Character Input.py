import datetime

date = datetime.datetime.now()

def NameAndAge():
    name = raw_input("What is your name?")
    age = raw_input("What is your age?")
    ageDiff = 100 - int(age)
    yearAge100 = int(date.year) + ageDiff
    print "So %s you will turn 100 in %d years (%d)" % (name,int(ageDiff),int(yearAge100))



NameAndAge()




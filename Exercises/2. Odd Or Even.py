



def CheckNumber():
    number = raw_input("Give me a number")
    if int(number) % 2 == 0:
        if int(number) % 4 == 0:
            times = int(number) / 4
            print "This is a Even number that can be divided by 4 ( 4 x %d = %d )" % (int(times), int(number))
        else:
            print 'This number is Even'
    else:
        print "The number is ODD"

while True:
    CheckNumber()
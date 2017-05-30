

def palindrome():
    word = raw_input("Give me a palindrome")
    invword = word[::-1]

    if word.lower() == invword.lower():
        print "Yes, this is a palindrome  # %s #" % (word)
    else:
        print "You did not enter a palindrome "


while True:
    palindrome()
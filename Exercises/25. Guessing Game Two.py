import random


def guess(low, high):
    guess = random.randint(low+1, high)
    print guess
    return guess



class game():
        def __init__(self):
            self.low = 0
            self.high = 100
            self.turns = 0
        def play(self):
            while True:
                self.guess = guess(self.low,self.high)
                answer = raw_input("\"H\"igher, \"L\"ower or \"C\"orrect")
                if answer == "h":
                    self.low = self.guess
                elif answer == "l":
                    self.high = self.guess
                elif answer == "c":
                    print "you won with {} turns".format(self.turns)
                    break
                self.turns += 1






GG2 = game()
GG2.play()

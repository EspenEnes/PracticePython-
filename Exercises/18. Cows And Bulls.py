import random
import Tkinter as tk
import threading



class CowBull(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.root = tk.Tk()

        # Variables
        self.answer = tk.IntVar()


        self.scoreLabel = tk.LabelFrame(self.root)
        self.scoreLabel.grid(column=0, row=1, rowspan=10, sticky=tk.N + tk.S)

        self.guessLabel = tk.LabelFrame(self.root)
        self.guessLabel.grid(column=1, row=1, rowspan=10, sticky=tk.W + tk.E)

        self.entryLabel = tk.Label(self.root)
        self.entryLabel.grid(column=2, row=1, rowspan=10)

        self.entry = []
        self.guess = []
        self.guessVariables = []
        for x in range(0,10):
            self.guessVariables.append(tk.IntVar())
            self.guess.append(tk.Label(self.guessLabel,textvariable=self.guessVariables[x]))
            self.guess[x].grid(row=x)

        self.answer = ([random.randint(0, 9) for x in range(0, 4)])
        self.guesses = 0
        self.entry = tk.Entry(self.root)
        self.entry.grid(row=11,column=2)







        self.QuitButton = tk.Button(self.root,text="Quit", command=self.root.quit)
        self.QuitButton.grid(row=11, column=3)

        self.guessButton = tk.Button(self.root, text="Guess", command=self.game)
        self.guessButton.grid(row=11, column=1)







        self.start()

    def run(self):
        self.root.mainloop()

    def get_guess(self):
        #guess = [int(x) for x in ((raw_input("guess the number")))]
        guess = [int(x) for x in self.entry.get()]
        print [x["text"] for x in self.guess]

        if len(guess) == 4:
            self.guessVariables[self.guesses].set(guess)
            return guess
        else:
            print "wrong length"
            #self.get_guess()

    def game(self):
            guess = self.get_guess()

            cow = 0
            bull = 0

            for i in range(0, 4):
                if self.answer[i] == guess[i]:
                    guess[i] = "cow"
                    cow += 1
                else:
                    if self.answer[i] in guess:
                        guess[guess.index(self.answer[i])] = "bull"
                        bull += 1

            self.guesses += 1
            self.roundscore = tk.Label(self.scoreLabel,text= "cow: " + str(cow) + " bull:" + str(bull))
            self.roundscore.grid(sticky=tk.N)

            print "cow: " + str(cow) + " bull:" + str(bull)

            if cow == 4:
                print "WWohoooooooooooooooooo    you win with {:d} guesses".format(self.guesses)
                game = False

            self.entry.delete(0,"end")







if __name__ == "__main__":
    game = CowBull()





































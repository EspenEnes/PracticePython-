import threading
from random import randint
import Tkinter as Tk



class GG1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.root = Tk.Tk()
        self.root.title("Guessing Game One")

        #Variables
        self.GuessVar = Tk.StringVar()
        self.Guesses = Tk.IntVar()
        self.GuessDisable = Tk.BooleanVar()



        self.GuessField = Tk.Frame(self.root)
        self.GuessField.pack()

        self.root.bind('<Return>', self.Guess1)

        self.GuessEntryLabel = Tk.Label(self.GuessField, text="Guess a number between 1-9")
        self.GuessEntryLabel.grid(row=0, column=0,columnspan=2)

        self.GuessEntry = Tk.Entry(self.GuessField, textvariable=self.GuessVar)
        self.GuessEntry.grid(row=1, column=1)

        self.GuessButton = Tk.Button(self.GuessField,text="Guess", state='normal' ,command=self.Guess)
        self.GuessButton.grid(row=1, column=0,sticky=Tk.W)

        self.guessesLabel1 = Tk.Label(self.GuessField, text="Guesses: ")
        self.guessesLabel1.grid(row=2, column=0)

        self.guessesLabel2 = Tk.Label(self.GuessField, textvariable=self.Guesses)
        self.guessesLabel2.grid(row=2, column=1, sticky=Tk.W)

        self.NewGameButton = Tk.Button(self.GuessField, text="New Game", command=self.new_game)
        self.NewGameButton.grid(row=3,column=0)

        self.ExitButton = Tk.Button(self.GuessField, text="Exit",command=self.root.quit)
        self.ExitButton.grid(row=3, column=1, sticky=Tk.E)

        self.new_game()






        self.start()

    def new_game(self):
        self.number = randint(1, 9)
        self.Guesses.set(0)
        self.GuessButton.config(state="normal")
        self.GuessEntry.config(state="normal")

    def Guess1(self, event):
        if self.GuessButton["state"] == "normal":
            self.Guess()

    def Guess(self):
        try:

            if int(self.GuessVar.get()) > self.number:
                self.Guesses.set(self.Guesses.get() + 1)
                print "Your guess is to high"
            elif int(self.GuessVar.get()) < self.number:
                self.Guesses.set(self.Guesses.get() + 1)
                print "Your guess is to low"
            else:
                print "Nailed it with " + str(self.Guesses.get())  + " guesses"
                self.GuessButton.config(state="disabled")
                self.GuessEntry.config(state="disabled")



        except:
            self.GuessVar.set("not a number")



    def run(self):


        self.root.mainloop()


test = GG1()
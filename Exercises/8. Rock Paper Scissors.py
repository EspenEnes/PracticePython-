import Tkinter as tk

P1Value = ""
P2Value = ""


def InitGame():
    if PlayButton["text"] == "Save":
        player1["state"] = "disabled"
        player2["state"] = "disabled"
        PlayButton["text"] = "Edit"
    else:
        player1["state"] = "normal"
        player2["state"] = "normal"
        PlayButton["text"] = "Save"

def StoreR():
    global P1Value
    P1Value = "R"
    print P1Value

def StoreS():
    global P1Value
    P1Value = "S"
    print P1Value

def StoreP():
    global P1Value
    P1Value = "P"
    print P1Value



root = tk.Tk()
root.title("Rock Paper Scissors")

UserField = tk.LabelFrame(root,text="Player Names")
UserField.grid(row=0)

PlayerField = tk.LabelFrame(root,text="Select")
PlayerField.grid(row=1)

player1 = tk.Entry(UserField)
player1.pack()
player2 = tk.Entry(UserField)
player2.pack()

PlayButton = tk.Button(UserField,text="Save",command=InitGame)
PlayButton.pack()

Player = tk.Label(PlayerField,text="Player1 select")
Player.pack()

Rock = tk.Button(PlayerField,text="Rock",command=StoreR)
Rock.pack()

Scissors = tk.Button(PlayerField,text="Scissors",command=StoreS)
Scissors.pack()

Paper = tk.Button(PlayerField,text="Paper",command=StoreP)
Paper.pack()



root.mainloop()






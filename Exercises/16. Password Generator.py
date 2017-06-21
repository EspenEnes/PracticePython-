import threading
import random
import Tkinter as tk


def PasswordGenerator():
    strength = HMI.passStrength.get()
    alfabetLower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alfabetUpper = " ".join(alfabetLower).upper().split()
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    password = []
    if strength < 25:
        list = alfabetLower
        length = random.randrange(3,5)
    elif strength > 75:
        list = alfabetLower + alfabetUpper + numbers
        length = random.randrange(10, 15)
    else:
        list = alfabetLower + alfabetUpper
        length = random.randrange(5,10)

    for x in range(0,length):
         password.append(random.choice(list))

    password = "".join(password)
    HMI.password.set(str(password))






class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)



        self.root = tk.Tk()

        # Variables
        self.password = tk.StringVar()

        self.header = tk.LabelFrame(self.root, text="Password strength")
        self.header.grid(row=0)

        self.passStrength = tk.Scale(self.header,from_=0,to=100, orient=tk.HORIZONTAL)
        self.passStrength.grid(row=0)

        self.genButton = tk.Button(self.header,text="Gennerate",command=PasswordGenerator)
        self.genButton.grid(row=1)

        self.output = tk.Entry(self.root,textvariable=self.password)
        self.output.grid(row=1)




        self.start()



    def run(self):
        self.root.mainloop()




if __name__ == "__main__":
    HMI = GUI()




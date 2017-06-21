import threading
import Tkinter as tk





class checkPrimality(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.root = tk.Tk()
        self.root.title = "Check Primality Functions"

        self.root.bind('<Return>', self.check)

        #Variables
        self.label = tk.StringVar()

        self.head = tk.Frame(self.root)
        self.head.grid(row=0)
        self.body = tk.Frame(self.root)
        self.body.grid(row=1)
        self.foot = tk.Frame(self.root)
        self.foot.grid(row=2)


        self.headlabel = tk.LabelFrame(self.head, text="Check Primality Function")
        self.headlabel.pack()

        self.entry = tk.Entry(self.headlabel)
        self.entry.pack()

        self.bodyLabel = tk.Label(self.head,textvariable=self.label)
        self.bodyLabel.pack()


        self.start()

    def check(self, event):
        try:
            self.prime = 1
            for x in range(2,int(self.entry.get())):
                if int(self.entry.get()) % x == 0:
                    self.prime = 0
            if self.prime == 1:
                self.label.set(str(self.entry.get() + " is a prime number"))
            else:
                self.label.set(str(self.entry.get() + " is just a number"))




        except:
            self.label.set("This is not a number!")




    def run(self):
        self.root.mainloop()



check =checkPrimality()
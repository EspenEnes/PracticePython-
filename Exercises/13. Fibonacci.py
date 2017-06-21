import Tkinter as tk
import threading


class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.root = tk.Tk()
        self.root.title = "Fibonacci"

        self.root.bind("<Return>",self.Fibonacci)

        # Variables
        self.result = tk.StringVar()


        self.HeadFrame = tk.LabelFrame(self.root,text="Fibonacci")
        self.HeadFrame.grid(row=0)

        self.FibonacciLabel = tk.Label(self.HeadFrame,text="Length: ")
        self.FibonacciLabel.grid(row=0,column=0)

        self.FibonacciEntry = tk.Entry(self.HeadFrame)
        self.FibonacciEntry.grid(row=0,column=1)

        self.FibonacciEntryResult = tk.Text(self.root, height=50)
        self.FibonacciEntryResult.grid(row=1)


        self.start()

    def Fibonacci(self, event):
        self.FibonacciEntryResult.delete(1.0,tk.END)
        length = int(self.FibonacciEntry.get())
        result = [1, 1]

        for x in range(2, length):
            add = result[-2] + result[-1]
            result.append(add)

        self.FibonacciEntryResult.insert(tk.END,result)

    def run(self):
        self.root.mainloop()













FibonacciGUI = GUI()

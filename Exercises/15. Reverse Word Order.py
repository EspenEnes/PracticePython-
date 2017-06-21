import Tkinter as tk

def reverse(event):
    text = wordEntry.get()
    output.delete(1.0,tk.END)
    split = text.split()
    rev = []
    result = ""

    while len(split) > 0:
        a = split.pop(-1)
        rev.append(a)
    result = " ".join(rev)











    output.insert(tk.END,result)


root = tk.Tk()
root.bind('<Return>', reverse)

headlabel = tk.LabelFrame(root,text="Reverse Word Order")
headlabel.pack()
wordEntry = tk.Entry(headlabel)
wordEntry.pack()

output = tk.Text(root)
output.pack()










root.mainloop()
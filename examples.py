from tkinter import *

root = Tk()
rows = []
# datagrid
for i in range(5):
    cols = []
    for j in range(4):
        e = Entry(relief=GROOVE)
        e.grid(row=i, column=j, sticky=NSEW)
        e.insert(END, '%d.%d' % (i, j))
        cols.append(e)
    rows.append(cols)
root.mainloop()



tk.Grid()
root.geometry("500x700")  # width x height
root.title("MGA802 Final project")  # Adding a title

l1 = tk.Label(my_w, text="Search", width=5, font=18)  # added one Label
l1.grid(row=1, column=1, padx=3, pady=10)

e1 = tk.Entry(my_w, width=35, bg="yellow", font=18)  # added one Entry box
e1.grid(row=1, column=2, padx=1)

b1 = tk.Button(my_w, text="Search", width=7, font=18, command=lambda: my_search())
b1.grid(row=1, column=3, padx=2)
my_w.mainloop()

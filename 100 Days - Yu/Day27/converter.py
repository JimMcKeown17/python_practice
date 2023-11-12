from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label. Note that we're pusing the "packer" to put the label on the screen.

input = Entry(width=10)
input.grid(column=1, row=0)

def calc():
    miles = float(input.get())
    kms = round(miles * 5/3,2)
    result_label.config(text=kms)

miles_label = Label(text ="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2,row=0)

equal_label = Label(text ="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0,row=1)

result_label = Label(text ="0", font=("Arial", 12, "bold"))
result_label.grid(column=1,row=1)

km_label = Label(text ="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2,row=1)

button = Button(text="Calculate", command=calc)
button.grid(column=1,row=2)

window.mainloop()
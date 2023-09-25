from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label. Note that we're pusing the "packer" to put the label on the screen.

my_label = Label(text ="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)

my_label.config(text="Newbie")

def button_clicked():
    input_text = input.get()
    my_label.config(text=input_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)

input = Entry(width=10)
input.grid(column=3, row=2)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2,row=0)






window.mainloop()
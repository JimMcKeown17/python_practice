from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Getting words

df = pd.read_csv("data/french_words.csv")
french_card = ""
english_card = ""
def new_card():
    global french_card
    global english_card
    i = random.randint(0, len(df) - 1)
    french_card = df.iloc[i]['French']
    english_card = df.iloc[i]['English']
    # print(f"Index: {i}")  # print the random index
    # print(f"French: {french_card}, English: {english_card}")  # print for debugging
    canvas.itemconfig(word_text, text=french_card, fill="black")  # set text color to black



# Creating a new window and configurations
window = Tk()
window.title("Flashy")
window.minsize(width=900, height=600)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

def flip_card():
    canvas.itemconfig(language_text, text="english", fill="black")
    canvas.itemconfig(word_text, text=english_card)

window.after(3000, func=flip_card)

front_card = ""
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=img)
language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text=french_card, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
new_card()

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=new_card)
button_wrong.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
button_right = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=new_card)
button_right.grid(row=1, column=1)

window.mainloop()

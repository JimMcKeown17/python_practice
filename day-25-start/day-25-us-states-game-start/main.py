import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

t = turtle.Turtle()

turtle.shape(image)


states = pd.read_csv("50_states.csv")
score = 0
list_states = states['state'].to_list()
guessed_states =[]
while score < 50:
    answer_state = screen.textinput(title=f"Guess the State ({score}/50)", prompt="What's another states's name?")
    if answer_state == "Exit":
        missing_states = [state for state in list_states if state not in guessed_states]

    if answer_state in list_states:
        x_cor = int(states[states['state'] == answer_state]['x'])
        y_cor = int(states[states['state'] == answer_state]['y'])
        t.penup()
        t.hideturtle()
        t.goto(x_cor,y_cor)
        t.write(answer_state)
        guessed_states.append(answer_state)
        score +=1
        if score == 50:
            print("You win!")

turtle.mainloop()

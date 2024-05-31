import turtle
import time

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-200, -200)
border_pen.pensize(3)
border_pen.pendown()

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -180)
player.setheading(90)

playerspeed = 30

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -180:
        x = -180
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 180:
        x = 180
    player.setx(x)

for side in range(4):
    border_pen.fd(400)
    border_pen.lt(90)

border_pen.hideturtle()

enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-160, 150)

enemyspeed = 5

while True:
    wn.update()
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    if enemy.xcor() > 280 or enemy.xcor() < -280:
        enemyspeed *= -1



    # Listen for keyboard events
    turtle.listen()
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")

    # Introduce a delay to control the game speed
    time.sleep(0.5)  # Adjust the sleep time as needed
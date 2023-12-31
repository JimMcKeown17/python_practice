# Space Invaders - Part 1
import turtle
import os
import math
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders - Kimani-style")

# Draw a border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("blue")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the player turtle

player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# # Create the enemy
# enemy = turtle.Turtle()
# enemy.color("red")
# enemy.shape("circle")
# enemy.penup()
# enemy.speed(0)
# enemy.setposition(-200,250)

enemyspeed = 2

#Choose a number of enemies
number_of_enemies = 5
#Create a list of enemies
enemies = []
#Add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x, y)

#Create the player's bullet
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)


bulletspeed = 20

#Define bullet state
#ready - read to fire
#fire - bullet is firing
bulletstate = "ready"


# Move our player left and right

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def move_up():
    y = player.ycor()
    y += playerspeed
    if y > 290:
        y = 290
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -290:
        y = -290
    player.sety(y)

def fire_bullet():
    #Declare bulletstate as a global if it needs to be changed
    global bulletstate

    #Move the bullet to just above the player
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# Create keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(fire_bullet, "space")


#Main game loop
while True:

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)

        if enemy.xcor() < -280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)

        # Check for collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

        # Check if enemy collides with player
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has reached the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"




turtle.mainloop()


# Make a turtle on the screen jump to a random location if a person is able to click it in time.
# The click should trigger the player’s score to accumulate.
# If the timer runs out before the turtle is clicked, the turtle will disappear and the game will display a message.

import turtle, random, time
import datetime

highscoreFile = open("highscores.txt", "a+")
lines = highscoreFile.readlines()
try:
    highscore = lines[-1]
except IndexError:
    highscore = "0"

def getCoor():
    return (random.randint(-120, 120), random.randint(-120, 120))


def click(x, y):
    global score
    score += 100
    global timeLeft
    timeLeft += 0.5
    t.goto(getCoor())
    size = random.randint(1, 20)
    if size >= 10:
        size = random.randint(1, 10) / 10
    t.shapesize(size, size)

turtle.screensize(100, 100)

t = turtle.Turtle()
text = turtle.Turtle()

start = time.time()
current = time.time()
text.penup()
text.goto((0, 200))
text.pendown()

t.color("orange")
t.shape("circle")

text.hideturtle()

try:
    time.sleep(1)
    text.write("Ready", font=("Monospace", 14, "normal"))
    time.sleep(1)
    text.clear()
    text.write("    Set", font=("Monospace", 14, "normal"))
    time.sleep(1)
    text.clear()
    text.write("        GO!", font=("Monospace", 14, "normal"))
    time.sleep(2)
    t.goto(getCoor())
    text.clear()
    text.write(f"Time Left: {str(round(60 - (current - start), 2))} seconds", align="center", font=("Monospace", 14, "normal"))

    score = 0
    timeLeft = 15
    t.onclick(click)

    while timeLeft > 0: #and score < 20:
        start = time.time()
        text.clear()
        text.write(f"Time Left: {str(round(timeLeft, 2))} seconds\nScore: {str(score)}", align="center", font=("Monospace", 14, "normal"))
        time.sleep(0.1)
        end = time.time()
        timeLeft -= end - start

    text.color("green")
    text.clear()
    text.write(f"Congrats! Your score is {str(score)}. To accumulate this tremendous score,\nyou played this game for {'%.2f' % (time.time() - start)} seconds!", align="center", font=("Monospace", 24, "normal"))
    time.sleep(5)
    if score > int(highscore):
        text.clear()
        text.write(f"Congrats! New High Score of {str(score)}!!!!!!!!!!!", align="center", font=("Monospace", 24, "normal"))
        highscoreFile.write(str(score))
except turtle.Terminator:
    exit()
"""
if score >= 20:
    text.color("green")
    text.clear()
    text.write(f"You won! It took you {str(round(current - start, 2))} seconds. ", align="center", font=("Monospace", 24, "normal"))
elif current - start >= 60:
    text.color("red")
    text.clear()
    text.write(f"You lost. Try again!", font=("Monospace", 24, "normal"))
"""
time.sleep(10)
import turtle
from random import randint

# Ana ekran
drawing_board = turtle.Screen()
drawing_board.bgcolor("black")
drawing_board.title("Game")

# Skor
score = 0
game_over = False

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(250, 250)
score_turtle.color("purple")
score_turtle.write(f"Skor: {score}", align="right", font=("Arial", 20, "bold"))

# Ana turtle
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("purple")

# Süre yazısı
turtle_instance_1 = turtle.Turtle()
turtle_instance_1.hideturtle()
turtle_instance_1.color("purple")
turtle_instance_1.penup()
turtle_instance_1.goto(0, 200)

def move_turtle():
    if not game_over:
        turtle_instance.penup()
        turtle_instance.goto(randint(-200, 0), randint(0, 200))

def click_turtle(x, y):
    if not game_over:
        update_score()

def update_score():
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(f"Skor: {score}", align="right", font=("Arial", 20, "bold"))

def countdown(t):
    global game_over
    turtle_instance_1.clear()
    if t >= 0:
        move_turtle()
        turtle_instance_1.write(f"Süre: {t}", align="center", font=("Arial", 24, "bold"))
        drawing_board.ontimer(lambda: countdown(t - 1), 1000)
    else:
        game_over = True
        turtle_instance.hideturtle()
        turtle_instance_1.clear()
        turtle_instance_1.write("Oyun Bitti!", align="center", font=("Arial", 28, "bold"))

turtle_instance.onclick(click_turtle)
countdown(10)
drawing_board.mainloop()


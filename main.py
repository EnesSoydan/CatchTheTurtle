import turtle
import random

screen=turtle.Screen()
is_game_over=False
score=0
FONT=('Arial',30,'normal')

turtle_list=[]

counter_turtle=turtle.Turtle()
score_turtle=turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()

    score_turtle.setposition(0,230)
    score_turtle.write(f"Score: 0",move=False,align="center",font=FONT)

def make_turtle(x,y):
    t=turtle.Turtle()

    def handle_click(x,y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write("Score: {}".format(score),move=False,align="center",font=FONT)
        print(x,y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x*10,y*10)
    t.pendown()
    turtle_list.append(t)

x_coordinates=[-20,-10,0,10,20]
y_coordinates=[20,10,0,-10]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not is_game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)

def countdown(time):
    global is_game_over
    counter_turtle.hideturtle()
    counter_turtle.penup()
    counter_turtle.setposition(0, 270)
    counter_turtle.clear()

    if time > 0:
        counter_turtle.clear()
        counter_turtle.write("Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        is_game_over = True
        counter_turtle.clear()
        hide_turtles()
        counter_turtle.write("Game Over!", align='center', font=FONT)

def start_game_up():
    global is_game_over
    is_game_over = False
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)

start_game_up()
turtle.mainloop()
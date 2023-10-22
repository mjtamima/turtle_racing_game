from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
usr_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win the race? Enter a color: ")

colors = ['red', 'green', 'orange', 'yellow', 'purple', 'blue']
y_positions = [-100, -70, -40, -10, 20, 50]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if usr_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == usr_bet:
                print(f"You've won. The winner of the race is the {winning_turtle} turtle.")
            else:
                print(f"You've lost. The winner of the race is the {winning_turtle} turtle.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

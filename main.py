from turtle import Turtle, Screen
from random import randint

screen = Screen()
is_race_one = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, enter a color")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_one = True

while is_race_one:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_one = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You have won! The {winning_color} turtle won the race!")
            else:
                print(f"You lost, {winning_color}, won")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

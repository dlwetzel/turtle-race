from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in all_turtles:
        rand_distance = random.randint(0, 10)
        racer.forward(rand_distance)
        if racer.xcor() >= 230:
            is_race_on = False
            if user_bet == racer.color()[0]:
                print("You won! Congrats!")
            else:
                print(f"Sorry {racer.color()[0]} was the winner.")

screen.exitonclick()

import random

from color import color_palette


import turtle as turtle_module
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
nums_of_dot = 4000

tim.setheading(225)
tim.forward(350*2)
tim.setheading(0)
for dot_count in range(1, nums_of_dot + 1):
    tim.dot(20, random.choice(color_palette))
    tim.forward(50)

    # if number of dot %20 == 0 -> jump to the begin of next line
    if dot_count % 20 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500*2)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
#     tim.color(random.choice(color_palette))
#
#
#     tim.begin_fill()
#     tim.circle(10)
#     turtle.setx(-200)
#     turtle.sety(200)
#
#     tim.end_fill()
#
# draw_circle()
import turtle
import turtle as t
import random

# COLORGRAM MODULE TO EXTRACT COLORS FROM IMAGES
# import colorgram
# rgb = cg.extract('./image.jpg', 20)
# colors = []

# for obj in rgb:
#     color = tuple([obj.rgb.r, obj.rgb.g, obj.rgb.b])
#     colors.append(color)

# print(colors)
tim = t.Turtle()
screen = t.Screen()
turtle.colormode(255)

tim.hideturtle()
tim.penup()
tim.goto(-230.00, -230.00)
tim.pendown()
tim.showturtle()

colors = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85),
          (226, 237, 228), (223, 137, 176), (144, 108, 56), (102, 197, 219),
          (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50),
          (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73),
          (4, 161, 86), (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221),
          (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8), (89, 48, 31)]


def print_color():
    tim.dot(20, random.choice(colors))
    tim.penup()
    tim.forward(50)
    tim.pendown()


def add_row():
    tim.penup()
    tim.goto(-230.00,tim.ycor() + 50)
    tim.pendown()


for _ in range(1,101):
    print_color()
    if _ % 10 == 0:
        add_row()

screen.exitonclick()

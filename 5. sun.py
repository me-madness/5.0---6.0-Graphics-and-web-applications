import turtle

my_turtle = turtle.Turtle()

# Change the shape of the turtle
my_turtle.shape("turtle")

for i in range(0, 36):
    my_turtle.color("orange")
    my_turtle.forward(250)
    my_turtle.right(178)
    my_turtle.left(3)
    
turtle.done()


# from turtle import *
# begin_fill()
# while True:
#     my_turtle.forward(200)
#     my_turtle.left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()    
# turtle.done   
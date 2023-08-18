import turtle

my_turtle = turtle.Turtle()

# Change the shape of the turtle
my_turtle.shape("turtle")

for i in range(0, 6):
    my_turtle.right(60)
    my_turtle.forward(100)
    
turtle.done()    
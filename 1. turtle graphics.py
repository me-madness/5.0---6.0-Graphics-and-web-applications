import turtle

my_turtle = turtle.Turtle()

# Change the shape of the turtle
my_turtle.shape("turtle")

for i in range(1, 3):
    # Draw a equilateral triangle
    my_turtle.left(30)
    my_turtle.forward(200)
    my_turtle.left(120)
    my_turtle.forward(200)
    my_turtle.left(120)
    my_turtle.forward(200)
    
turtle.done()    
    
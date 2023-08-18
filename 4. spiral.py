import turtle

my_turtle = turtle.Turtle()

# Change the shape of the turtle
my_turtle.shape("turtle")
step = 20
for i in range(0, 20):
    my_turtle.forward(step)
    my_turtle.right(60)
    step += 5
    
turtle.done()
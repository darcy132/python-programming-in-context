import turtle

def draw_star(size):
    angle = 144  # The angle between each point of the star
    turtle.color("blue")  # You can change the color of the star
    turtle.begin_fill()  # Begin filling the star with the specified color
    for _ in range(5):
        turtle.forward(size)  # Move the turtle forward by the specified size
        turtle.right(angle)  # Turn the turtle to the right by the specified angle
    turtle.end_fill()  # End filling the star

# Set up the turtle screen
turtle.speed(10)  # Set the turtle speed (1 is slowest, 10 is fastest)
turtle.bgcolor("black")  # Set the background color of the turtle screen

# Draw a star with size 100
draw_star(100)

# Close the turtle graphics window when clicked
turtle.done()

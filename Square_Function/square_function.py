# square_function.py
# Square Function

import turtle

def square(x, y, size, color):
    turtle.color(color)                             # Set the color of the square.
    turtle.penup()                                  # Lift the turtle pen up.
    turtle.goto(x, y)                               # Move the turtle to coords x, y.
    turtle.pendown()                                # Set the turtle pen down.
    
    turtle.begin_fill()                             # Fill the next shape drawn.
    for n in range(4):                              # Loop to draw the square.
        turtle.forward(size)                        # Move the turtle forward.
        turtle.left(90)                             # Turn the turtle left 90 degrees.
    turtle.end_fill()                               # Fill in the square.

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.bgcolor("white")                         # Set background color to white.
    
    # Draw some squares.
    square(100, 140, -360, "purple")
    square(300, 250, -240, "red")
    square(250, -50, -200, "yellow")
    square(-50, 200, -300, "blue")

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":
    main()

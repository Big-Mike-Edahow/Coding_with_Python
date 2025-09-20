# color_spin.py
# Random Color Spin

import turtle
import random

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=640, height=480)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.width(120)                               # Set the line width to 120 pixels.
    turtle.bgcolor("white")                         # Set background color to white.
    
    # List of paint colors.
    paint = ["red", "blue", "yellow", "green", "orange", "pink"]
    
    # Loop to draw the dots.
    for angle in range(0, 360, 10):
        turtle.goto(0, 0)                           # Move the turtle to the center.
        turtle.color(random.choice(paint))          # Random color choice from paint list.
        turtle.seth(angle)                          # Point the turtle in random direction.
        turtle.forward(800)                         # Draw a line 800 pixels long.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

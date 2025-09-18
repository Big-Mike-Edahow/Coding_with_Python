# chopsticks.py
# Random Colored Lines

import turtle
import random

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=640, height=480)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.width(6)                                 # Set the line width to 6 pixels.
    turtle.bgcolor("white")                         # Set background color to white.
    
    # List of paint colors.
    paint = ["red", "blue", "yellow", "green", "orange", "pink"]
    
    # Loop to draw the dots.
    for n in range(100):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        turtle.goto(x, y)                           # Move the turtle to random position.
        angle = random.randint(0, 360)              # Random angle to turn the turtle.
        length = random.randint(150, 250)           # How far the turtle will move.
        turtle.color(random.choice(paint))          # Random color choice from paint list.
        turtle.seth(angle)                          # Point the turtle in random direction.
        turtle.forward(length)                      # Draw a line as long as length.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

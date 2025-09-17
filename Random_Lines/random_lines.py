# random_lines.py
# Random Lines

import turtle
import random

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=640, height=480)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.width(10)                                # Set the line width to 10 pixels.
    turtle.bgcolor("white")                         # Set background color to white.
    
    # List of paint colors.
    paint = ["red", "blue", "yellow", "green", "orange", "pink"]
    
    # Loop to draw the lines.
    for n in range(100):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        turtle.color(random.choice(paint))
        turtle.goto(x, y)

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

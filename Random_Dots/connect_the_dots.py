# connect_the_dots.py
# Random Dots

import turtle
import random

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    size = random.randint(10, 30)                   # Set the dot size to random number.
    turtle.pencolor("black")                        # Set the pencolor to black.
    turtle.bgcolor("white")                         # Set background color to white.
    
    # Loop to draw the dots.
    for n in range(30):
        x = random.randint(0, 300)
        y = random.randint(0, 300)
        turtle.goto(x, y)
        turtle.dot(size)

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

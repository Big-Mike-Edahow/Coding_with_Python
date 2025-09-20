# random_hoops.py
# Random Hoops

import turtle                                       # Import the Turtle graphics library.
import random                                       # Import the Random library.

def main():    
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=640, height=480)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.bgcolor("white")                         # Set background color to white.
    
    # List of paint colors.
    paint = ["red", "blue", "yellow", "green", "orange", "pink"]
    
    # Loop to draw the dots in steps of -10.
    for size in range(400, 0, -10):
        turtle.color(random.choice(paint))
        turtle.dot(size)

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

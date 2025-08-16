# random_dots.py
# A Bit Random

import turtle
import random

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.bgcolor("black")                         # Set background color to black.
    
    # List of color choices.
    paint = ["red", "green", "blue", "pink", "orange", "yellow"]
    
    # Loop to draw the dots.
    for n in range(100):
        size = random.randint(20, 100)
        color = random.choice(paint)
        x = random.randint(0, (screen.window_width() // 2) - (size // 2))
        y = random.randint(0, (screen.window_height() // 2 ) - (size // 2))
        turtle.goto(x, y)
        turtle.pencolor(color)
        turtle.dot(size)
        turtle.penup()

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.

if __name__ == "__main__":                          # Main entry point of the program.
    main()

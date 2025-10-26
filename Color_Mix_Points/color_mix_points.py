# color_mix_points.py
# Color Mix Points

import turtle
import random

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=640, height=480)             # Define the window size.
    turtle.penup()                                  # Don't draw lines in between each dot.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.colormode(255)                           # Use color values between 0 and 255.
    turtle.bgcolor("white")                         # Set background color to white.                                  # Set the dot size to 50 pixels.
    
    # Loop to draw the color points.
    for c in range(0, 255):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        turtle.goto(x, y)
        turtle.color(255, c, 0)
        turtle.dot(20)

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

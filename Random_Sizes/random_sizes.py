# random_sizes.py
# Random Sizes

import turtle
import random

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=640, height=480)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.penup()                                  # Lift the pen so no lines are drawn.
    turtle.bgcolor("white")                         # Set background color to white.
    
    # List of paint colors.
    paint = ["red", "blue", "yellow", "green", "orange", "pink"]
    
    # Loop to draw the dots.
    for n in range(50):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        size = random.randint(40, 200)              # Set the dot size to random.
        turtle.color(random.choice(paint))          # Random color choice from paint list.
        turtle.goto(x, y)
        turtle.dot(size)

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

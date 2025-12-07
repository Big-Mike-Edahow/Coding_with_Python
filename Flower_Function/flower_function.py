# flower_function.py
# Flower Function

import turtle
import random

def flower(x, y, petalColor):
    turtle.penup()                                  # Lift the turtle pen up.
    turtle.goto(x, y)                               # Move the turtle to coords x, y.
    turtle.pendown()                                # Set the turtle pen down.
    turtle.width(5)                                 # Set the line width to 5.
    turtle.seth(90)                                 # Point the turtle up.
    turtle.color("green")                           # Choose green for the stem.
    turtle.forward(70)                              # Draw the flower's stem.

    for n in range(5):                              # Loop to draw the petals.
        turtle.width(25)                            # Set the line width to 25.
        turtle.right(72)                            # Turn right 72 degrees.
        turtle.color(petalColor)                    # Set the petal color.
        turtle.forward(25)                          # Draw one petal.
        turtle.back(25)                             # Move back the the flower's center.

    turtle.color("black")                           # Set the color to black.
    turtle.dot(30)                                  # Draw the flower's center.

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.bgcolor("lightgreen")                    # Set background color to light green.
    
    petalColors = ["red", "purple", "yellow"]       # Petal colors list.
    
    for f in range(20):                             # Loop to draw the flowers.
        x = random.randint(-300, 300)               # Random x coordinate.
        y = random.randint(-300, 300)               # Random y coordinate.
        flower(x, y, random.choice(petalColors))    # Draw a random flower.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":
    main()

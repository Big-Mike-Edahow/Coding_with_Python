# sprinkled_donut.py
# Sprinkled Donut

import turtle                                       # Import the Turtle graphics library.
import random                                       # Import the Random library.

def main():    
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=620)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.colormode(255)                           # Use color values from 0 to 255.
    turtle.bgcolor("light blue")                    # Set background color to light blue.
    
    turtle.color(209, 154, 98)                      # Mix a light brown donut color.
    turtle.dot(580)                                 # Draw the donut.
    turtle.color("pink")                            # Pink for the icing.
    turtle.dot(530)                                 # Draw the icing.
    turtle.color("light blue")                      # Select the background color again.
    turtle.dot(220)                                 # Make a hole in the donut.
    
    colorList = ["white", "yellow", "magenta"]      # List of colors for sprinkles.
    turtle.width(10)                                # Set the width of the sprinkles.
    
    # Loop to draw the sprinkles.
    for sprinkle in range(60):
        turtle.seth(sprinkle * 6)                   # Spread the sprinkles every 6 degrees.
        turtle.penup()                              # lift the pen up.
        turtle.goto(0, 0)                           # Move the turtle to the center.
        turtle.forward(random.randint(150, 230))    # Move forward a random distance.
        turtle.seth(random.randint(1, 360))         # Face a random direction
        turtle.color(random.choice(colorList))      # Pick a random sprinkle color.
        turtle.pendown()                            # Set the pen down.
        turtle.forward(32)                          # Draw a sprinkle.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

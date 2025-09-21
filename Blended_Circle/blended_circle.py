# blended_circle.py
# Blended Circle

import turtle

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=620)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.width(3)                                 # Set the line width to 3 pixels.
    turtle.colormode(255)                           # Use color values from 0 to 255.
    turtle.bgcolor("white")                         # Set background color to white.
    
    # Loop to draw the blended circle.
    for a in range(0, 180):
        turtle.goto(0, 0)                           # Move the turtle to window's center.
        turtle.color(255, a, 0)                     # Set the color using the variable a.
        turtle.right(2)                             # Rotate 2 degees clockwise.
        turtle.forward(300)                         # Draw a line 300 pixels from center.
        
    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

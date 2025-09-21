# gradient_square.py
# Gradient Square

import turtle

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=640, height=480)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.colormode(255)                           # Use color values from 0 to 255.
    turtle.bgcolor("white")                         # Set background color to white.
    
    # Calculate starting position for a centered square
    side_length = 200
    start_x = - (side_length / 2)
    start_y = - (side_length / 2)
    
    # Loop to draw the blended square.
    for x in range(0, 200):
        turtle.color(255, 128, x)                   # Random color choice from paint list.
        turtle.goto(start_x, start_y)               # Gradually move the turtle sideways.
        turtle.goto(start_x, (start_y + 200))       # Draw a line up to 200 pixels.
        start_x = start_x + 1                       # Increment the x position by 1.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":
    main()

# blended_square.py
# Blended Square

import turtle

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=640, height=480)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.colormode(255)                           # Use color values from 0 to 255.
    turtle.bgcolor("white")                         # Set background color to white.
    
    # Loop to draw the blended square.
    for x in range(0, 200):
        turtle.color(255, 128, x)                   # Random color choice from paint list.
        turtle.goto(x, 0)                           # Gradually move the turtle sideways.
        turtle.goto(x, 200)                          # Draw a line up to 200 pixels.
        
    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

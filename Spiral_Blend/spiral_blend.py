# spiral_blend.py
# Spiral Blend

import turtle

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.colormode(255)                           # Use color values between 0 and 255.
    turtle.width(1)                                 # Set the line width to 1 pixel.
    turtle.bgcolor("white")                         # Set background color to white.
    
    for n in range(255):
        turtle.pencolor(255, 255 - n, n)            # Set the color based on the n variable.
        turtle.forward(n * 2)                       # Move the turtle forward n * 2.
        turtle.right(91)                            # Turn right 90 degrees.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.

if __name__ == "__main__":                          # Main entry point of the program.
    main()

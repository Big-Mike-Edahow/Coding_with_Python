# recursive_spiral.py
# Recursive Spiral

import turtle                                       # Import the Turtle graphics library.

def drawSpiral(side):
    turtle.forward(side)                            # Draw a line the length of side.
    turtle.right(45)                                # Turn right 45 degrees.
    if (side > 10):                                 # Recursively draw another line.
        drawSpiral(side - 5)                        

def main():    
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.bgcolor("red")                           # Set background color to red.
    turtle.color("orange")                          # Set orange as the color.
    turtle.width(15)                                # Set the line width to 15;
    turtle.penup()                                  # Lift the turtle pen up.
    turtle.goto(-125, 230)                          # Go to the starting coords.
    turtle.pendown()                                # Set the turtle pen down.
    drawSpiral(200)                                 # Initial side length is 200.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.
    
if __name__ == "__main__":                          # Main entry point of the program.
    main()


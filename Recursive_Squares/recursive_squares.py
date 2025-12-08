# recursive_squares.py
# Recursive Squares

import turtle

def drawSquare(x, y, width, color):
    turtle.penup()                                  # Lift the turtle pen up.
    turtle.goto(x, y)                               # Move the turtle to coords x, y.
    turtle.pendown()                                # Set the turtle pen down.
    turtle.color(color, color)                      # Set the line and fill color.
    
    turtle.begin_fill()                             # Fill the next shape drawn.
    for n in range(4):                              # Loop to draw the square.
        turtle.forward(width)                       # Move the turtle forward.
        turtle.right(90)                            # Turn the turtle right 90 degrees.
    turtle.end_fill()                               # Fill in the square.

    if (color == "blue"):                           # Alternate the square colors.                          
        color = "yellow"
    else:
        color = "blue"
    if (width > 20):                                # Recursively draw another square.
        drawSquare(x + 10, y - 10, width - 20, color)

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.bgcolor("black")                         # Set background color to black.
    
    # Start drawing the squares.
    drawSquare(-200, 200, 400, "blue")

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":
    main()


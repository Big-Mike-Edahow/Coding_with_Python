# circles.py
# Spinning Circles

import turtle

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.bgcolor("black")                         # Set background color to black.
    
    turtle.pencolor("red")                          # Set the pen color to red.
    for circle in range(60):                        # Loop to draw the outer circles.
        for n in range(36):
            turtle.forward(25)
            turtle.right(10)
        turtle.right(6)
    
    turtle.pencolor("gold")                         # Set the pen color to gold.
    for circle in range(30):                        # Loop to draw the inner circles.
        for n in range(36):
            turtle.forward(20)
            turtle.right(10)
        turtle.right(12)

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.

if __name__ == "__main__":                          # Main entry point of the program.
    main()


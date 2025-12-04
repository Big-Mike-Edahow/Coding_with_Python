# spiral_list.py
# Spiral List

import turtle

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.width(1)                                 # Set the line width to 1 pixel.
    turtle.bgcolor("black")                         # Set background color to black.
    
    # Create a list of colors.
    colorList = ['red', 'blue', 'green', 'cyan', 'purple', 'yellow', 'pink', 'orange']
        
    for n in range(300):
        turtle.color(colorList[n%8])                # Set the color based on the n variable.
        turtle.forward(n)                           # Move the turtle forward n steps.
        turtle.right(61)                            # Turn right 61 degrees.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.

if __name__ == "__main__":                          # Main entry point of the program.
    main()

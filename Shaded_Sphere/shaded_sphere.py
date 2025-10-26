# shaded_sphere.py
# Shaded Sphere

import turtle

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=640, height=600)             # Define the window size.
    turtle.colormode(255)                           # Use color values from 0 to 255.
    turtle.bgcolor("white")                         # Set background color to white.
    
    # Loop to draw the shaded sphere.
    for size in range(255, 0, -1):                  # Loop counting down from 255 to 0.
        turtle.color(255, 128, size)                # Set color using the size variable.
        turtle.dot(2 * size)                        # Draw a dot two times size.
        
    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

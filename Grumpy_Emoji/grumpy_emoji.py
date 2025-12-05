# grumpy_emoji.py
# Grumpy Emoji

import turtle

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.bgcolor("white")                         # Set background color to white.
    
    turtle.penup()                                  # Don't draw lines.
    turtle.color("yellow")                          # Select yellow for the face color.
    turtle.dot(420)                                 # Draw a large dot to make the face.
    
    turtle.color("black")                           # Select black for the eyes.
    turtle.goto(80, 70)                             # Move up and to the right.
    turtle.dot(40)                                  # Draw the right eye.
    turtle.goto(-80, 70)                            # Move to the left.
    turtle.dot(40)                                  # Draw the left eye.
    
    turtle.goto(0, -90)                             # Move to the center and down.
    turtle.dot(160)                                 # Draw a medium sized dot for the mouth.
    turtle.color("yellow")                          # Change to yellow for the smile.
    turtle.goto(0, -120)                             # Move up a little bit.
    turtle.dot(180)                                 # Draw a medium black dot for the smile.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.

if __name__ == "__main__":                          # Main entry point of the program.
    main()

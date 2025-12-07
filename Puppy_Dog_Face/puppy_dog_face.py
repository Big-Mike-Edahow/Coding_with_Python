# puppy_dog_face.py
# Puppy Dog Face

import turtle

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.colormode(255)                           # Color values from 0 to 255;
    turtle.bgcolor("blue")                          # Set background color to blue.
    
    # Face
    turtle.penup()                                  # Don't draw lines.
    turtle.color(177, 127, 74)                      # Select brown for the dogs color.
    turtle.dot(150)                                 # Draw a large dot to make the face.
    
    # Eyes
    turtle.color("white")                           # Select white for the left outer eye.
    turtle.goto(-30, 30)                            # Move up and to the left.
    turtle.dot(40)                                  # Draw the left eyeball.
    turtle.color("black")                           # Select black for the pupil
    turtle.dot(25)                                  # Draw the left pupil.
    turtle.color("white")                           # Select white for the right outer eye.
    turtle.goto(30, 30)                             # Move to the right.
    turtle.dot(40)                                  # Draw the right outer eye.
    turtle.color("black")                           # Select black for the pupil
    turtle.dot(25)                                  # Draw the right pupil.
    
    # Muzzle
    turtle.goto(0, -40)                             # Move to the center and down.
    turtle.color(202, 158, 103)                     # Light brown color for the muzzle.
    turtle.dot(80)                                  # Draw the dog's muzzle.
                     
    # Nose        
    turtle.goto(0, -10)                             # Move just below the center.
    turtle.color("black")                           # Set the color to black for the nose.
    turtle.dot(30)                                  # Draw the nose.
    
    # Left ear
    turtle.width(40)                                # Set the line width the 40 pixels.
    turtle.goto(-80, 20)                            # Move turtle to draw the left ear.
    turtle.color(104, 60, 17)                       # Set the color to dark brown.
    turtle.pendown()                                # Get ready to draw.
    turtle.seth(270)                                # Point the turtle downwards.
    turtle.forward(90)                              # Draw the left ear.
    turtle.penup()                                  # Lift the pen up.
    
    # Right ear
    turtle.width(40)                                # Set the line width the 40 pixels.
    turtle.goto(80, 20)                             # Move turtle to draw the right ear.
    turtle.color(104, 60, 17)                       # Set the color to dark brown.
    turtle.pendown()                                # Get ready to draw.
    turtle.seth(270)                                # Point the turtle downwards.
    turtle.forward(90)                              # Draw the right ear.
    turtle.penup()                                  # Lift the pen up.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.

if __name__ == "__main__":                          # Main entry point of the program.
    main()

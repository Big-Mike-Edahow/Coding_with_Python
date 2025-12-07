# puppy_dog_body.py
# Puppy Dog Body

import turtle

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=900, height=600)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.penup()                                  # Lift the turtle pen up.
    turtle.colormode(255)                           # Color values from 0 to 255;
    turtle.bgcolor("blue")                          # Set background color to blue.
    
    # Body
    turtle.width(150)                               # A wide line for the body.
    turtle.color(147, 96, 55)                       # Darker shade of brown for the body.
    turtle.goto(-100, -20)                          # Move just below the middle of the head.
    turtle.pendown()                                # Set the turtle pen down.
    turtle.goto(250, -20)                           # Draw the body across to the right.
    
    # Hind legs
    turtle.width(60)                                # Thinner lines for the legs.
    turtle.goto(300, -250)                          # Move down to draw the first hind leg.
    turtle.goto(250, -20)                           # Move back up to the body.
    turtle.goto(200, -250)                          # Draw the other hind leg.
    
    # Tail
    turtle.width(20)                                # Set the thickness for the tail.
    turtle.goto(300, 0)                             # Move to the start of the tail.
    turtle.goto(380, 120)                           # Draw the tail.
    turtle.penup()                                  # Lift the turtle pen up.
    
    # Front Legs
    turtle.width(60)                                # Set the width for the front legs.
    turtle.goto(-100, -20)                          # Move to the front of the body.
    turtle.pendown()                                # Set the turtle pen down.
    turtle.goto(-150, -250)                         # Draw the first front leg.
    turtle.goto(-100, -20)                          # Move back up to the body.
    turtle.goto(-50, -250)                          # Draw the other front leg.
    turtle.penup()                                  # lift the turtle pen up.
    
    # Face
    turtle.goto(-100, 100)                          # Move to the center to draw the face.                       
    turtle.color(177, 127, 74)                      # Select brown for the dogs color.
    turtle.dot(170)                                 # Draw a large dot to make the face.
    
    # Eyes
    turtle.color("white")                           # Select white for the left outer eye.
    turtle.goto(-130, 130)                          # Move up and to the left.
    turtle.dot(40)                                  # Draw the left eyeball.
    turtle.color("black")                           # Select black for the pupil
    turtle.dot(25)                                  # Draw the left pupil.
    turtle.color("white")                           # Select white for the right outer eye.
    turtle.goto(-70, 130)                           # Move to the right.
    turtle.dot(40)                                  # Draw the right outer eye.
    turtle.color("black")                           # Select black for the pupil
    turtle.dot(25)                                  # Draw the right pupil.
    
    # Muzzle
    turtle.goto(-100, 60)                           # Move to the center and down.
    turtle.color(202, 158, 103)                     # Light brown color for the muzzle.
    turtle.dot(80)                                  # Draw the dog's muzzle.
                     
    # Nose
    turtle.color("black")                           # Black for the nose and mouth.        
    turtle.goto(-100, 90)                           # Move just below the center.
    turtle.dot(30)                                  # Draw the nose.
    
    # Mouth
    turtle.goto(-110, 50)                           # Move down and left for the mouth.
    turtle.width(35)                                # Line thickness for the mouth.
    turtle.pendown()                                # Set the turtle pen down.
    turtle.goto(-90, 50)                            # Draw the mouth.
    turtle.penup()                                  # Lift the turtle pen up.
    
    # Left ear
    turtle.width(40)                                # Set the line width the 40 pixels.
    turtle.goto(-180, 120)                          # Move turtle to draw the left ear.
    turtle.color(104, 60, 17)                       # Set the color to dark brown.
    turtle.pendown()                                # Get ready to draw.
    turtle.seth(270)                                # Point the turtle downwards.
    turtle.forward(90)                              # Draw the left ear.
    turtle.penup()                                  # Lift the pen up.
    
    # Right ear
    turtle.width(40)                                # Set the line width the 40 pixels.
    turtle.goto(-20, 120)                           # Move turtle to draw the right ear.
    turtle.color(104, 60, 17)                       # Set the color to dark brown.
    turtle.pendown()                                # Get ready to draw.
    turtle.seth(270)                                # Point the turtle downwards.
    turtle.forward(90)                              # Draw the right ear.
    turtle.penup()                                  # Lift the pen up.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.

if __name__ == "__main__":                          # Main entry point of the program.
    main()

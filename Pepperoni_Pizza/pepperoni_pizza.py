# pepperoni_pizza.py
# Pepperoni Pizza

import turtle                                       # Import the Turtle graphics library.
import random                                       # Import the Random library.

def main():    
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=620)             # Define the window size.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.colormode(255)                           # Use color values from 0 to 255.
    turtle.bgcolor("light green")                   # Set background color to light green.
    
    turtle.color(209, 154, 98)                      # Mix a light brown color for the dough.
    turtle.dot(580)                                 # Draw the pizza pie.
    turtle.color("red")                             # Red for the tomato sauce.
    turtle.dot(510)                                 # Add some sauce to the pizza.
    turtle.color("yellow")                          # Yellow for the cheese.
    turtle.dot(480)                                 # Add some cheese to the pizza.
    turtle.penup()                                  # lift the pen up.
    
    # Loop to draw the pepperoni.
    for pepperoni in range(15):
        turtle.goto(0, 0)                           # Move the turtle to the center.
        turtle.seth(random.randint(1, 360))         # Face a random direction.      
        turtle.forward(random.randint(50, 200))     # Move forward a random distance.
        turtle.color("red")                         # Red for the pepperonis.
        turtle.dot(80)                              # Draw a pepperoni.

    # Loop to draw the black olives.
    for olive in range(20):
        turtle.goto(0, 0)                           # Move the turtle to the center.
        turtle.seth(random.randint(1, 360))         # Face a random direction.      
        turtle.forward(random.randint(50, 200))     # Move forward a random distance.
        turtle.color("black")                       # Black for the olives.
        turtle.dot(30)                              # Draw an olive.

    turtle.color("red")                             # Red for where the pizza is sliced.
    turtle.width(10)                                # Set the width of the cut.
    
    for slice in range(0, 360, 45):                 # Loop to slice the pizza.
        turtle.goto(0, 0)                           # Move to the center.
        turtle.pendown()                            # Set the pen down.
        turtle.seth(slice)                          # Point the turtle in correct direction.
        turtle.forward(285)                         # Slice the pizza.

    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.


if __name__ == "__main__":                          # Main entry point of the program.
    main()

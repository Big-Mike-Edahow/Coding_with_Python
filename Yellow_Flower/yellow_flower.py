# yellow_flower.py
# Yellow Flower

import turtle

def main():
    screen = turtle.Screen()                        # Create the graphics window.
    screen.setup(width=800, height=600)             # Define the window size.
    turtle.color("green")                           # Set the turtle color to green.
    turtle.bgcolor("blue")                          # Set background color to blue.
    turtle.speed(0)                                 # Set drawing speed to fastest.
    turtle.width(20)                                # Set the line width to 20 pixels.
    turtle.goto(0, -200)                            # 200 pixels below center.
    turtle.seth(90)                                 # Point the turtle upwards.
    turtle.forward(300)                             # Draw a line to be the flower stem.
        
    for n in range(5):
        turtle.width(90)                            # Set the width to 90 pixels.
        turtle.right(72)                            # Turn right 72 degrees.
        turtle.color("orange")                      # Set the color to orange.
        turtle.forward(50)                          # Move forward to draw the petal.
        turtle.back(50)                             # Move back to the center.
    
    turtle.color("red")                             # Set the color to red.
    turtle.dot(75)                                  # Draw the center of the flower.
    turtle.hideturtle()                             # Hide the cursor.  
    turtle.done()                                   # Keep the window open till closed.

if __name__ == "__main__":                          # Main entry point of the program.
    main()

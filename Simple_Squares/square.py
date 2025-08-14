# square.py
# Simple Squares

import turtle

def main():
    # Define the window size
    screen = turtle.Screen()
    screen.setup(width=500, height=400)
    
    # Set drawing speed to fastest
    turtle.speed(0)

    # Define the side length of the square
    side_length = 200

    # Set the pen color
    turtle.pencolor("red")
    
    # Set the line width
    turtle.width(20)

    # Lift the pen and move to the starting position for a centered square
    turtle.penup()
    turtle.goto(-side_length / 2, -side_length / 2)
    turtle.pendown()

    # Draw the square
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)

    # Hide the cursor
    turtle.hideturtle()
    
    # Keep window open    
    turtle.done()


if __name__ == "__main__":
    main()

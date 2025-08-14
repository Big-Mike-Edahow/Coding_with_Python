# squares.py
# Square Patterns

import turtle

def main():
    # Define the window size.
    screen = turtle.Screen()
    screen.setup(width=500, height=400)
    
    # Set drawing speed to fastest.
    turtle.speed(0)

    # Set line width and pen color.
    turtle.width(3)
    turtle.pencolor("purple")
    
    # Loop to draw the squares.
    for s in range(36):
        turtle.right(10)
        for n in range(4):
            turtle.forward(100)
            turtle.right(90)

    # Hide the cursor.
    turtle.hideturtle()
    
    # Keep window open.  
    turtle.done()


if __name__ == "__main__":
    main()

# multi.py
# Multi Patterns

import turtle

def main():
    # Define the window size.
    screen = turtle.Screen()
    screen.setup(width=720, height=540)
    
    # Set drawing speed to fastest.
    turtle.speed(0)

    # Set line width and pen color.
    turtle.width(4)
    turtle.pencolor("red")
    
    # Loop to draw the squares.
    for s in range(36):
        turtle.right(10)
        for n in range(4):
            turtle.forward(160)
            turtle.right(90)

    turtle.width(4)
    turtle.pencolor("orange")
    for s in range(36):
        turtle.right(10)
        for n in range(4):
            turtle.forward(120)
            turtle.right(90)

    turtle.width(4)
    turtle.pencolor("yellow")
    for s in range(36):
        turtle.right(10)
        for n in range(4):
            turtle.forward(80)
            turtle.right(90)
    
    # Hide the cursor.
    turtle.hideturtle()
    
    # Keep window open.  
    turtle.done()


if __name__ == "__main__":
    main()

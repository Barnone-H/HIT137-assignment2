import turtle

# Recursive function to draw the tree
def grow_tree(length, level, angleL, angleR, shrink, total_levels):
    if level == 0:
        return

    # Use brown color for the trunk, green for branches
    if level == total_levels:
        turtle.color("brown")
    else:
        turtle.color("green")

    # Make the pen size smaller as we go up the tree
    pen_thickness = max(2, int(8 * (level / total_levels)))
    turtle.pensize(pen_thickness)

    turtle.forward(length)  # draw the current branch

    # Save the current state so we can come back after drawing each side
    pos = turtle.position()
    angle = turtle.heading()

    # Draw the left branch
    turtle.left(angleL)
    grow_tree(length * shrink, level - 1, angleL, angleR, shrink, total_levels)

    # Go back to the previous position
    turtle.penup()
    turtle.setpos(pos)
    turtle.setheading(angle)
    turtle.pendown()

    # Draw the right branch
    turtle.right(angleR)
    grow_tree(length * shrink, level - 1, angleL, angleR, shrink, total_levels)

    # Reset position again just to be safe
    turtle.penup()
    turtle.setpos(pos)
    turtle.setheading(angle)
    turtle.pendown()

def main():
    # Get user inputs for tree customization
    angleL = float(input("Enter left branch angle (degrees): "))
    angleR = float(input("Enter right branch angle (degrees): "))
    start_len = float(input("Enter trunk length (pixels): "))
    total = int(input("How many levels deep? (recursion depth): "))
    ratio = float(input("Length reduction factor (e.g. 0.7): "))

    # Set up the drawing screen
    turtle.setup(800, 600)
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.left(90)  # Point turtle upward
    turtle.penup()
    turtle.goto(0, -250)  # Start from bottom center
    turtle.pendown()

    # Start drawing the tree
    grow_tree(start_len, total, angleL, angleR, ratio, total)

    turtle.done()

if __name__ == "__main__":
    main()

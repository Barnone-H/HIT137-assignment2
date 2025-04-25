import turtle

# Define the recursive function to draw the tree
def draw_tree(branch_length, depth, left_angle, right_angle, reduction_factor):
    if depth == 0:
        return

    # Draw the main branch
    turtle.forward(branch_length)

    # Save the current position and heading
    current_position = turtle.position()
    current_heading = turtle.heading()

    # Draw the left branch
    turtle.left(left_angle)
    draw_tree(branch_length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)

    # Go back to the saved position and heading
    turtle.penup()
    turtle.setposition(current_position)
    turtle.setheading(current_heading)
    turtle.pendown()

    # Draw the right branch
    turtle.right(right_angle)
    draw_tree(branch_length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)

    # After finishing both sides, return to the original position
    turtle.penup()
    turtle.setposition(current_position)
    turtle.setheading(current_heading)
    turtle.pendown()


def main():
    # Take user input
    left_angle = float(input("Enter the left branch angle (in degrees): "))
    right_angle = float(input("Enter the right branch angle (in degrees): "))
    start_length = float(input("Enter the starting branch length (in pixels): "))
    depth = int(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7 for 70%): "))

    # Set up the turtle screen
    turtle.setup(width=800, height=600)
    turtle.bgcolor("white")
    turtle.color("green")
    turtle.speed(0)  # Fastest speed
    turtle.left(90)  # Point the turtle upwards
    turtle.penup()
    turtle.goto(0, -250)  # Start at the bottom center
    turtle.pendown()

    # Start drawing the tree
    draw_tree(start_length, depth, left_angle, right_angle, reduction_factor)

    # Finish
    turtle.done()

if __name__ == "__main__":
    main()

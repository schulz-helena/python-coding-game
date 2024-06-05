import turtle
import time


screen = turtle.Screen()
screen.title("Maze Game")
screen.setup(width=800, height=650)
screen.colormode(255)
screen.tracer(0)
screen.bgcolor((255, 205, 178))


GRID_SIZE = 50  


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
]

# Draw the maze
def draw_maze(maze):
    turtle.speed(0)
    turtle.penup()
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            screen_x = -350 + (x * GRID_SIZE)
            screen_y = 280 - (y * GRID_SIZE)
            if maze[y][x] == 1:
                turtle.goto(screen_x, screen_y)
                turtle.color((229, 152, 155))
                turtle.pendown()
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(GRID_SIZE)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
            if maze[y][x] == 3:
                turtle.goto(screen_x, screen_y)
                turtle.color((255, 183, 0))
                turtle.pendown()
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(GRID_SIZE)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
    turtle.hideturtle()

draw_maze(maze)


player = turtle.Turtle()
player.shape("arrow")  
player.shapesize(1.5)  #
player.color((120, 150, 100))
player.penup()
player.speed(0)
player.goto(-320 + (1 * GRID_SIZE), 260 - (0 * GRID_SIZE))  
player.direction = "down" 
player.setheading(270)

def move():
    if can_move_forward():
        player.forward(GRID_SIZE)


def can_move_forward():

    next_x, next_y = player.position()
    if player.direction == "up":
        next_y += GRID_SIZE
    elif player.direction == "right":
        next_x += GRID_SIZE
    elif player.direction == "down":
        next_y -= GRID_SIZE
    elif player.direction == "left":
        next_x -= GRID_SIZE


    grid_x = int((next_x + 320) / GRID_SIZE)
    grid_y = int((260 - next_y) / GRID_SIZE)
    
    return (0 <= grid_x < len(maze[0]) and 0 <= grid_y < len(maze) and maze[grid_y][grid_x] == 0) or maze[grid_y][grid_x] == 3

def check_goal():
    next_x, next_y = player.position()  
    grid_x = int((next_x + 320) / GRID_SIZE)
    grid_y = int((260 - next_y) / GRID_SIZE)    

    return maze[grid_y][grid_x] == 3

def rotate_left():
    if player.direction == "up":
        player.direction = "left"
        player.setheading(180)
    elif player.direction == "right":
        player.direction = "up"
        player.setheading(90)
    elif player.direction == "down":
        player.direction = "right"
        player.setheading(0)
    elif player.direction == "left":
        player.direction = "down"
        player.setheading(270)

def rotate_right():
    if player.direction == "up":
        player.direction = "right"
        player.setheading(0)
    elif player.direction == "right":
        player.direction = "down"
        player.setheading(270)
    elif player.direction == "down":
        player.direction = "left"
        player.setheading(180)
    elif player.direction == "left":
        player.direction = "up"
        player.setheading(90)

# Main game loop
def main():
    screen.listen()

    while not check_goal():
        rotate_right()

        while not can_move_forward():
            rotate_left()
        
        move()

        time.sleep(0.2)

        screen.update()

if __name__ == "__main__":
    main()
    turtle.done()

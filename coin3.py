import sys
import turtle
import time
from PyQt5.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
GAME_WIDTH = 800

screen = turtle.Screen()
screen.title("Maze Game")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.colormode(255)
screen.tracer(0)
screen.bgcolor((255, 205, 178))

GRID_SIZE = 50

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

def replace_zeros_with_negatives(maze, count):
    # Find all positions of 0 in the maze
    zero_positions = [(i, j) for i, row in enumerate(maze) for j, value in enumerate(row) if value == 0]
    

    # Randomly select the positions to replace
    positions_to_replace = random.sample(zero_positions, count)

    # Replace the selected positions with -1
    for i, j in positions_to_replace:
        maze[i][j] = -1

    return maze

def draw_maze(maze):

    turtle.clear()
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
            elif maze[y][x] == 3:
                turtle.goto(screen_x, screen_y)
                turtle.color((255, 183, 0))
                turtle.pendown()
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(GRID_SIZE)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
            elif maze[y][x] == -1:
                turtle.goto(screen_x + GRID_SIZE / 2, screen_y - GRID_SIZE / 2)
                turtle.color((255, 255, 0))
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(GRID_SIZE / 4)
                turtle.end_fill()
                turtle.penup()
    turtle.hideturtle()

maze = replace_zeros_with_negatives(maze, 10)
draw_maze(maze)

player = turtle.Turtle()
player.shape("arrow")
player.shapesize(1.5)
player.color((120, 150, 100))
player.penup()
player.speed(0)
player.goto(-320 + (1 * GRID_SIZE), 260 - (1 * GRID_SIZE))
player.setheading(270)
player.direction = "down"

def move_up():
    player.setheading(90)
    player.direction = "up"
    if can_move_forward():
        player.forward(GRID_SIZE)
        handle_coin_collection()
        screen.bgcolor((255, 205, 178))
        screen.update()
        time.sleep(0.5)
    else:
        print("Verloren!")

def move_down():
    player.setheading(270)
    player.direction = "down"
    if can_move_forward():
        player.forward(GRID_SIZE)
        handle_coin_collection()
        screen.bgcolor((255, 205, 178))
        screen.update()
        time.sleep(0.5)
    else:
        print("Verloren!")

def move_left():
    player.setheading(180)
    player.direction = "left"
    if can_move_forward():
        player.forward(GRID_SIZE)
        handle_coin_collection()
        screen.bgcolor((255, 205, 178))
        screen.update()
        time.sleep(0.5)
    else:
        print("Verloren!")

def move_right():
    player.setheading(0)
    player.direction = "right"
    if can_move_forward():
        player.forward(GRID_SIZE)
        handle_coin_collection()
        screen.bgcolor((255, 205, 178))
        screen.update()
        time.sleep(0.5)
    else:
        print("Verloren!")

def check_goal():
    next_x, next_y = player.position()
    grid_x = int((next_x + 320) / GRID_SIZE)
    grid_y = int((260 - next_y) / GRID_SIZE)
    if maze[grid_y][grid_x] == 3:
        return True
    
    return False

def move():
    if can_move_forward():
        player.forward(GRID_SIZE)
        #handle_coin_collection()
        screen.bgcolor((255, 205, 178))
        screen.update()
        time.sleep(0.5)

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

    return (0 <= grid_x < len(maze[0]) and 0 <= grid_y < len(maze) and maze[grid_y][grid_x] in [0, -1, 3])

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

def handle_coin_collection():
    next_x, next_y = player.position()
    grid_x = int((next_x + 320) / GRID_SIZE)
    grid_y = int((260 - next_y) / GRID_SIZE)
    if maze[grid_y][grid_x] == -1:
        maze[grid_y][grid_x] = 0
        draw_maze(maze)
        print("Coin collected!")

def is_onCoin():
    next_x, next_y = player.position()
    grid_x = int((next_x + 320) / GRID_SIZE)
    grid_y = int((260 - next_y) / GRID_SIZE)
    if maze[grid_y][grid_x] == -1:
        return True

# PyQt5 Application
class CodeEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.runButton = QPushButton('Run Code', self)
        self.runButton.clicked.connect(self.run_code)
        
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.runButton)
        self.setLayout(layout)
        
        self.setWindowTitle('Code Editor')
        self.setGeometry(GAME_WIDTH + 10, 10, 380, SCREEN_HEIGHT)
    
    def run_code(self):
        code = self.textEdit.toPlainText()
        try:
            exec(code, globals())
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = CodeEditor()
    editor.show()
    turtle.listen()
    turtle.onkey(move_up, "Up")
    turtle.onkey(move_down, "Down")
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")
    turtle.onkey(rotate_left, "a")
    turtle.onkey(rotate_right, "d")
    screen.update()
    sys.exit(app.exec_())

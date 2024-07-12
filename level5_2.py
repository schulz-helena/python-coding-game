import sys
import turtle
import time
from PyQt5.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox
import random
import os

# Setup screen:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
GAME_WIDTH = 800
GRID_SIZE = 50

screen = turtle.Screen()
screen.title("Level 5.2")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.colormode(255)
screen.tracer(0)
screen.bgcolor((255, 205, 178)) 


# Setup and draw maze:
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, -1, 1, 0, 1, -1, 1, 0, -1, 0, 0, 1, -1, 1],
    [1, 0, -1, 0, 1, 0, 0, 0, 1, 1, 0, -1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, -1, 1, 0, 1, 0, -1, 1, 0, -1, 1, -1, 0, 1],
    [1, 1, 1, 0, 1, -1, 0, -1, 0, 0, 1, 0, -1, 1],
    [1, -1, 0, -1, 1, -1, 0, -1, 1, 0, 1, 1, 0, 1],
    [1, -1, 1, 1, 1, 1, 1, 1, 1, 0, 1, -1, 0, 1],
    [1, 0, 1, -1, 0, -1, 0, 0, 0, 0, 1, 0, 3, 1],
    [1, 0, 0, 0, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1],
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
                turtle.pencolor((150,150,150))
                for _ in range(4):
                    turtle.forward(GRID_SIZE)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
            if maze[y][x] == 0:
                turtle.goto(screen_x, screen_y)
                turtle.color((255, 205, 178))
                turtle.pendown()
                turtle.begin_fill()
                turtle.pencolor((150,150,150))
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
                turtle.pencolor((150,150,150))
                for _ in range(4):
                    turtle.forward(GRID_SIZE)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
            if maze[y][x] == -1:
                turtle.goto(screen_x, screen_y)
                turtle.color((255, 205, 178))
                turtle.pendown()
                turtle.begin_fill()
                turtle.pencolor((150,150,150))
                for _ in range(4):
                    turtle.forward(GRID_SIZE)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
                
                turtle.goto(screen_x + GRID_SIZE / 2, screen_y - GRID_SIZE / 2 - GRID_SIZE / 4)
                turtle.color((255, 255, 0))
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(GRID_SIZE / 4)
                turtle.end_fill()
                turtle.penup()
    turtle.hideturtle()

draw_maze(maze)


# Setup player:
player = turtle.Turtle()
player.shape("arrow")  
player.shapesize(1.5)
player.color((120, 150, 100))
player.penup()
player.speed(0)
player.goto(-320 + (1 * GRID_SIZE), 260 - (1 * GRID_SIZE))
player.setheading(270)
player.direction = "down" 


# Helper variables and functions:
game_running = True

def update_screen():
    screen.bgcolor((255, 205, 178))
    screen.update()
    time.sleep(0.1)


# Functions that are usable in code editor:
def goal_reached():
    next_x, next_y = player.position()
    grid_x = round((next_x + 320) / GRID_SIZE)
    grid_y = round((260 - next_y) / GRID_SIZE)
    if maze[grid_y][grid_x] == 3:
        return True
    
    return False


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

    # Convert floating-point position to grid coordinates
    grid_x = round((next_x + 320) / GRID_SIZE)
    grid_y = round((260 - next_y) / GRID_SIZE)

    # Ensure grid coordinates are within the maze boundaries
    if 0 <= grid_x < len(maze[0]) and 0 <= grid_y < len(maze):
        return maze[grid_y][grid_x] == 0 or maze[grid_y][grid_x] == 3 or maze[grid_y][grid_x] == -1
    else:
        return False

def move():
    global game_running
    if game_running:
        if can_move_forward():
            player.forward(GRID_SIZE)
            update_screen()
        else:
            game_running = False

def rotate_left():
    global game_running
    if game_running:
        if player.direction == "up":
            player.direction = "left"
            player.setheading(180)
            update_screen()
        elif player.direction == "right":
            player.direction = "up"
            player.setheading(90)
            update_screen()
        elif player.direction == "down":
            player.direction = "right"
            player.setheading(0)
            update_screen()
        elif player.direction == "left":
            player.direction = "down"
            player.setheading(270)
            update_screen()

def rotate_right():
    global game_running
    if game_running:
        if player.direction == "up":
            player.direction = "right"
            player.setheading(0)
            update_screen()
        elif player.direction == "right":
            player.direction = "down"
            player.setheading(270)
            update_screen()
        elif player.direction == "down":
            player.direction = "left"
            player.setheading(180)
            update_screen()
        elif player.direction == "left":
            player.direction = "up"
            player.setheading(90)
            update_screen()

global collected
collected = 0


def collect_coin():
    next_x, next_y = player.position()
    grid_x = round((next_x + 320) / GRID_SIZE)
    grid_y = round((260 - next_y) / GRID_SIZE)
    if maze[grid_y][grid_x] == -1:
        maze[grid_y][grid_x] = 0
        draw_maze(maze)
        global collected
        collected += 1
        update_screen()
        


def is_on_coin():
    next_x, next_y = player.position()
    grid_x = round((next_x + 320) / GRID_SIZE)
    grid_y = round((260 - next_y) / GRID_SIZE)
    if maze[grid_y][grid_x] == -1:
        return True
    
# PyQt5 Application with code editor window:
class CodeEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.textEdit = QTextEdit(self)
        if os.path.exists(os.path.join("saved_code", "code5_2.txt")):
            with open(os.path.join("saved_code", "code5_2.txt"), "r") as f:
                defaultText = f.read()
        else:
            defaultText = ""
        self.textEdit.setPlainText(defaultText)
        self.runButton = QPushButton('Run Code', self)
        self.runButton.clicked.connect(self.run_code)
        
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.runButton)
        self.setLayout(layout)
        
        self.setWindowTitle('Code Editor')
        self.setGeometry(GAME_WIDTH + 10, 10, 480, SCREEN_HEIGHT)
    
    def run_code(self):
        global game_running
        game_running = True
        code = self.textEdit.toPlainText()
        if not os.path.exists("saved_code"):
            os.makedirs("saved_code")
        with open(os.path.join("saved_code", "code5_2.txt"), "w") as f:
            f.write(code)
        try:
            exec(code, globals())
            if not game_running:
                screen.bgcolor((255, 205, 178))
                screen.update()
                self.ran_into_wall_popup()
                player.goto(-320 + (1 * GRID_SIZE), 260 - (1 * GRID_SIZE)) 
                player.setheading(270)
                player.direction = "down" 
            else:
                if goal_reached():
                    self.won_popup()
                else:
                    screen.bgcolor((255, 205, 178))
                    screen.update()
                    self.goal_not_reached_popup()
                    player.goto(-320 + (1 * GRID_SIZE), 260 - (1 * GRID_SIZE))
                    player.setheading(270)
                    player.direction = "down" 
    
        except Exception as e:
            print(e)

    def goal_not_reached_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Ziel nicht erreicht")
        msg.setText("Du hast das Ziel leider nicht erreicht.")
        msg.setStandardButtons(QMessageBox.Retry)
        x = msg.exec_()

    def ran_into_wall_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Gegen die Wand gelaufen")
        msg.setText("Du bist gegen die Wand gelaufen. Versuche es nochmal!")
        msg.setStandardButtons(QMessageBox.Retry)
        x = msg.exec_()

    def won_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Gewonnen")
        msg.setText("Herzlichen Glückwunsch, du hast das Level geschafft! Du hast " + str(collected) + " Münzen gesammelt!")
        close_button = msg.addButton("Level beenden", QMessageBox.AcceptRole)

        with open("level_5.2.status", "w") as f:
            f.write("COMPLETED")

        msg.exec_()
        if msg.clickedButton() == close_button:
            sys.exit()


# Main game loop:
def main():
    screen.listen()

    app = QApplication(sys.argv)
    editor = CodeEditor()
    editor.show()

    running = True
    while running:
        screen.update()
    
    turtle.done()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

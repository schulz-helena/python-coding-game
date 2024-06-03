import sys
import turtle
import time
from PyQt5.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget, QPushButton

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
player.shapesize(1.5)
player.color((120, 150, 100))
player.penup()
player.speed(0)
player.goto(-320 + (1 * GRID_SIZE), 260 - (0 * GRID_SIZE))  
player.direction = "down" 
player.setheading(270)

def move_up():
    player.setheading(90)
    player.forward(GRID_SIZE)
    check_goal()
    screen.bgcolor((255, 205, 178))
    screen.update()
    time.sleep(0.5)

def move_down():
    player.setheading(270)
    player.forward(GRID_SIZE)
    check_goal()
    screen.bgcolor((255, 205, 178))
    screen.update()
    time.sleep(0.5)

def move_left():
    player.setheading(180)
    player.forward(GRID_SIZE)
    check_goal()
    screen.bgcolor((255, 205, 178))
    screen.update()
    time.sleep(0.5)

def move_right():
    player.setheading(0)
    player.forward(GRID_SIZE)
    check_goal()
    screen.bgcolor((255, 205, 178))
    screen.update()
    time.sleep(0.5)

def check_goal():
    next_x, next_y = player.position()
    grid_x = int((next_x + 320) / GRID_SIZE)
    grid_y = int((260 - next_y) / GRID_SIZE)
    if maze[grid_y][grid_x] == 3:
        print("Goal reached!")


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
            print(e)

# Main game loop
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

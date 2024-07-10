import sys
import turtle
import time
from PyQt5.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox, QLabel
import re
import copy


# Setup screen:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
GAME_WIDTH = 800
GRID_SIZE = 50

screen = turtle.Screen()
screen.title("Maze Game")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.colormode(255)
screen.tracer(0)
screen.bgcolor((255, 205, 178)) 


# Setup and draw maze:
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, -4, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, -2, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, -1, 0, 1, 0, 1, 1],
    [1, 1, -5, 1, 0, 1, 1, 1, 1, 1, 1, -3, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
original_maze = copy.deepcopy(maze)


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
            elif maze[y][x] < 0: 
                turtle.goto(screen_x + GRID_SIZE / 2, screen_y - GRID_SIZE / 2 - GRID_SIZE / 4)
                turtle.color((255, 255, 0))
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(GRID_SIZE / 4)
                turtle.end_fill()
                turtle.penup()
                turtle.goto(screen_x + GRID_SIZE / 2, screen_y - GRID_SIZE / 2 - 10) 
                turtle.color((0, 0, 0))
                turtle.write(str(-maze[y][x]), align="center", font=("Arial", 12, "bold"))
    turtle.hideturtle()



draw_maze(maze)


# Setup player:
player = turtle.Turtle()
player.shape("arrow")  
player.shapesize(1.5)
player.color((120, 150, 100))
player.penup()
player.speed(0)
player.goto(-320 + (6 * GRID_SIZE), 260 - (5 * GRID_SIZE))  
player.setheading(0)
player.direction = "right" 


# Helper variables and functions:
game_running = True
coord_sums = []

def update_screen():
    screen.bgcolor((255, 205, 178))
    screen.update()
    time.sleep(0.5)


# Functions that are usable in code editor:
def goal_reached():
    next_x, next_y = player.position()
    # Convert floating-point position to grid coordinates
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
        return maze[grid_y][grid_x] == 0 or maze[grid_y][grid_x] == 3 or maze[grid_y][grid_x] < 0
    else:
        return False

def is_onCoin():
    next_x, next_y = player.position()
    grid_x = round((next_x + 320) / GRID_SIZE)
    grid_y = round((260 - next_y) / GRID_SIZE)
    if maze[grid_y][grid_x] < 0:
        return True
    return False

def pick_up_coin():
    next_x, next_y = player.position()
    grid_x = round((next_x + 320) / GRID_SIZE)
    grid_y = round((260 - next_y) / GRID_SIZE)
    if maze[grid_y][grid_x] < 0:
        coin_id = maze[grid_y][grid_x] * -1
        maze[grid_y][grid_x] = 0
        draw_maze(maze)
        return coin_id
    
def get_position():
    next_x, next_y = player.position()
    grid_x = round((next_x + 320) / GRID_SIZE)
    grid_y = round((260 - next_y) / GRID_SIZE)
    return [grid_x, grid_y]
    
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


# PyQt5 Application with code editor window:
class CodeEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("Füge die Summe der Koordinaten jeder der Münzen zur Liste hinzu und sortiere sie aufsteigend, bevor du das Ziel erreichst!")
        self.label.setStyleSheet("font-weight: bold; color: rgb(229, 152, 155)")
        self.label.setWordWrap(True)
        self.textEdit = QTextEdit(self)
        solution = "# Diese Zeile bitte nicht löschen:\ncoord_sums = []\n\nwhile not goal_reached():\n\tif not can_move_forward():\n\t\trotate_left()\n\telse:\n\t\tmove()\n\t\tif is_onCoin():\n\t\t\tcoords = get_position()\n\t\t\tsum = coords[0] + coords[1]\n\t\t\tcoord_sums.append(sum)\n\t\t\tcoord_sums.sort()"
        defaultText = "# Diese Zeile bitte nicht löschen:\ncoord_sums = []"
        self.textEdit.setPlainText(defaultText)
        self.runButton = QPushButton('Run Code', self)
        self.runButton.clicked.connect(self.run_code)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.runButton)
        self.setLayout(layout)
        
        self.setWindowTitle('Code Editor')
        self.setGeometry(GAME_WIDTH + 10, 10, 380, SCREEN_HEIGHT)
    
    def run_code(self):
        global maze
        global game_running
        game_running = True
        global coord_sums
        code = self.textEdit.toPlainText()
        try:
            exec(code, globals())
            # Coin coordinates: [8,5] [6,3] [11,6] [3,1] [2,6], Sums: 13 9 17 4 8
            print(coord_sums)
            if coord_sums == [4, 8, 9, 13, 17]:
                paradigm_used = True
            else: paradigm_used = False
            if not game_running:
                screen.bgcolor((255, 205, 178))
                screen.update()
                self.ran_into_wall_popup()
                player.goto(-320 + (6 * GRID_SIZE), 260 - (5 * GRID_SIZE)) 
                player.setheading(0)
                player.direction = "right"
                draw_maze(original_maze)
                maze = copy.deepcopy(original_maze)
            else:
                if goal_reached():
                    if paradigm_used:
                        self.won_popup()
                    else:
                        self.goal_no_win_popup()
                        player.goto(-320 + (6 * GRID_SIZE), 260 - (5 * GRID_SIZE))   
                        player.setheading(0)
                        player.direction = "right"
                        draw_maze(original_maze)
                        maze = copy.deepcopy(original_maze)
                else:
                    screen.bgcolor((255, 205, 178))
                    screen.update()
                    self.goal_not_reached_popup()
                    player.goto(-320 + (6 * GRID_SIZE), 260 - (5 * GRID_SIZE))   
                    player.setheading(0)
                    player.direction = "right"
                    draw_maze(original_maze)
                    maze = copy.deepcopy(original_maze)
        except Exception as e:
            print(e)

    def goal_not_reached_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Ziel nicht erreicht")
        msg.setText("Du hast das Ziel leider nicht erreicht. Versuche es nochmal!")
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
        msg.setText("Herzlichen Glückwunsch, du hast das Level geschafft!")
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()
    
    def goal_no_win_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Koordinaten-Summen sind nicht richtig sortiert")
        msg.setText("Du hast das Ziel erreicht, aber deine Liste von Koordinaten-Summen ist nicht korrekt. Versuche es nochmal!")
        msg.setStandardButtons(QMessageBox.Retry)
        x = msg.exec_()


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
    
import sys
import pygame
import time
from PyQt5.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget, QPushButton

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_WIDTH = 800
PLAYER_SIZE = 50
PLAYER_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coding Game")

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (GAME_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE)
        self.test = False
        
    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= 10
            screen.fill(BACKGROUND_COLOR)
            all_sprites.draw(screen)
            pygame.display.flip()
            time.sleep(0.5)

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10
            screen.fill(BACKGROUND_COLOR)
            all_sprites.draw(screen)
            pygame.display.flip()
            time.sleep(0.5)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
            screen.fill(BACKGROUND_COLOR)
            all_sprites.draw(screen)
            pygame.display.flip()
            time.sleep(0.5)

    def move_right(self):
        if self.rect.right < GAME_WIDTH:
            self.rect.x += 10
            screen.fill(BACKGROUND_COLOR)
            all_sprites.draw(screen)
            pygame.display.flip()
            time.sleep(0.5)

# Sprite groups
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


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

def main():
    app = QApplication(sys.argv)
    editor = CodeEditor()
    editor.show()
    
    # Game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update display
        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(30)
    
    pygame.quit()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

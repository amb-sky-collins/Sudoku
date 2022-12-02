import sudoku_generator
from sudoku_generator import Cell
from sudoku_generator import *
import pygame

# Variables
width = 630
height = 630
bg_color = (255, 255, 246)

# Initializing pygame
pygame.init() # pygame window
pygame.display.set_caption('Sudoku') # caption for that window
board = Board(width, height, screen=pygame.display.set_mode((width, height)), difficulty=0)  # Change difficulty later


# Main function
def main():
    board.screen.fill(bg_color)
    board.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()


if __name__ == '__main__':
    main()

from sudoku_generator import *
from sys import *
import pygame

# Initializing pygame
pygame.init() # pygame window
pygame.display.set_caption('Sudoku') # caption for that window
board = Board(width, height, screen=pygame.display.set_mode((width, height), row=0, col=0), difficulty=0)  # Change difficulty later


# referred to https://youtu.be/U9H60qtw0Yg for game_start(screen) method
# displays game start screen with easy, medium, and hard difficulty levels
def game_start(screen):
    title_font = pygame.font.Font(None, 90)
    prompt_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 70)
    screen.fill(bg_color) # fills screen with background color
    surf_title = title_font.render("Welcome to Sudoku", 0, line_color) # text
    surf_rect1 = surf_title.get_rect(center=(width // 2, height // 2 - 150)) # position
    screen.blit(surf_title, surf_rect1)
    surf_prompt = prompt_font.render("Select Game Mode", 0, line_color) # text
    surf_rect2 = surf_prompt.get_rect(center=(width // 2, height // 2 + 20)) # position
    screen.blit(surf_prompt, surf_rect2)

    easy_text = button_font.render("Easy", 0, (255, 255, 255)) # text
    medium_text = button_font.render("Medium", 0, (255, 255, 255)) # text
    hard_text = button_font.render("Hard", 0, (255, 255, 255)) # text

    easy_surf = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surf.fill(line_color)
    easy_surf.blit(easy_text, (10, 10))
    medium_surf = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surf.fill(line_color)
    medium_surf.blit(medium_text, (10, 10))
    hard_surf = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surf.fill(line_color)
    hard_surf.blit(hard_text, (10, 10))

    easy_rect = easy_surf.get_rect(center=(width // 3 - 75, height // 2 + 150)) # position
    medium_rect = medium_surf.get_rect(center=(width // 2, height // 2 + 150)) # position
    hard_rect = hard_surf.get_rect(center=(width // 2 + 180, height // 2 + 150)) # position

    screen.blit(easy_surf, easy_rect)
    screen.blit(medium_surf, medium_rect)
    screen.blit(hard_surf, hard_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit() # stops loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    # Checks if mouse is on easy button
                    return  # If the mouse is on the start button, we can return to main
                elif medium_rect.collidepoint(event.pos): # If the mouse is on the medium button, return
                    return
                elif hard_rect.collidepoint(event.pos): # If the mouse is on the hard button, return
                    return
                # TODO: UPDATE RETURNS LATER

        pygame.display.update()


# Main function
def main():
    board.screen.fill(bg_color)
    board.draw()
    game_start(screen=pygame.display.set_mode((width, height)))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() # removes error message when window is closed by stopping while True loop

        pygame.display.update()


if __name__ == '__main__':
    main()

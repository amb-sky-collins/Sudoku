from sudoku_generator import *
from sys import *
import pygame

screen = pygame.display.set_mode((width, height))
# Initializing pygame
pygame.init() # pygame window
pygame.display.set_caption('Sudoku') # caption for that window
board = Board(width, height, screen, row=0, col=0, difficulty=0)  # Change difficulty later


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
                exit()  # stops loop
            global removed_cells
            removed_cells = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    # Checks if mouse is on easy button
                    removed_cells = 30
                    return  # If the mouse is on the start button, we can return to main
                elif medium_rect.collidepoint(event.pos): # If the mouse is on the medium button, return
                    removed_cells = 40
                    return
                elif hard_rect.collidepoint(event.pos): # If the mouse is on the hard button, return
                    removed_cells = 50
                    return

        pygame.display.update()

def game_in_progress_buttons(screen):
    button_font = pygame.font.Font(None, 50)
    # Creates reset button
    reset_text = button_font.render('Reset', True, font_color)
    reset_surf = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surf.fill(button_color)
    reset_surf.blit(reset_text, (10, 10))
    reset_rect = reset_surf.get_rect(center=(width // 3 - 75, height // 2 + 315))
    screen.blit(reset_surf, reset_rect)
    # Creates restart button
    restart_text = button_font.render('Restart', True, font_color)
    restart_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surf.fill(button_color)
    restart_surf.blit(restart_text, (10, 10))
    restart_rect = restart_surf.get_rect(center=(width // 3 + 110, height // 2 + 315))
    screen.blit(restart_surf, restart_rect)
    # Creates exit button
    exit_text = button_font.render('Exit', True, font_color)
    exit_surf = pygame.Surface((exit_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    exit_surf.fill(button_color)
    exit_surf.blit(exit_text, (10, 10))
    exit_rect = exit_surf.get_rect(center=(width // 3 + 290, height // 2 + 315))
    screen.blit(exit_surf, exit_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # removes error message when window is closed by stopping while True loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # Determines coordinates of cell being clicked
                clicked_cell = board.click(x, y)  # Determines the row and col of the cell being clicked
                board.select(clicked_cell[0], clicked_cell[1])
                if reset_rect.collidepoint(event.pos):
                    pass
                elif restart_rect.collidepoint(event.pos):
                    pass
                elif exit_rect.collidepoint(event.pos):
                    exit()

        pygame.display.update()

def game_won(screen):
    title_font = pygame.font.Font(None, 90)
    button_font = pygame.font.Font(None, 70)
    screen.fill(bg_color) # fills screen with background color
    end_title = title_font.render("Game Won!", 0, line_color) # text
    end_surf = end_title.get_rect(center=(width // 2, height // 2 - 150)) # position
    screen.blit(end_title, end_surf)

    exit_text = button_font.render("Exit", 0, (255, 255, 255)) # text
    exit_surf = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surf.fill(line_color)
    exit_surf.blit(exit_text, (10, 10))
    exit_rect = exit_surf.get_rect(center=(width // 2, height // 2 + 150)) # position
    screen.blit(exit_surf, exit_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()  # stops loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(event.pos):
                    exit()  # stops loop

        pygame.display.update()

def game_over(screen):
    title_font = pygame.font.Font(None, 90)
    button_font = pygame.font.Font(None, 70)
    screen.fill(bg_color) # fills screen with background color
    end_title = title_font.render("Game Over :(", 0, line_color) # text
    end_surf = end_title.get_rect(center=(width // 2, height // 2 - 150)) # position
    screen.blit(end_title, end_surf)

    restart_text = button_font.render("Restart", 0, (255, 255, 255)) # text
    restart_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surf.fill(line_color)
    restart_surf.blit(restart_text, (10, 10))
    restart_rect = restart_surf.get_rect(center=(width // 2, height // 2 + 150)) # position
    screen.blit(restart_surf, restart_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()  # stops loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    screen.fill(bg_color)
                    board.draw()
                    game_in_progress_buttons(screen)


        pygame.display.update()


# Main function
def main():
    game_start(screen)
    board.screen.fill(bg_color)
    board.draw()

    # generate_sudoku(9, removed_cells) # generates board TODO: HOW TO DISPLAY THIS ON THE BOARD?

    """
    if the board is full and all the numbers match the solution:
        game_won(screen)
    elif the board is full and the numbers don't match the solution:
        game_over(screen)
    """

    game_over(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # removes error message when window is closed by stopping while True loop

        pygame.display.update()


if __name__ == '__main__':
    main()

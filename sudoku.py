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
    while True:
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
            value = None
            prev_clicked_cell = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()  # removes error message when window is closed by stopping while True loop
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos  # Determines coordinates of cell being clicked
                    clicked_cell = board.click(x, y)  # Determines the row and col of the cell being clicked

                    # Selects cell, deselects previous cell if new cell is selected
                    if prev_clicked_cell is None:
                        board.select(clicked_cell[0], clicked_cell[1])
                    elif prev_clicked_cell == clicked_cell:
                        pass
                    else:
                        board.deselect(prev_clicked_cell[0], prev_clicked_cell[1])
                        board.select(clicked_cell[0], clicked_cell[1])

                    if reset_rect.collidepoint(event.pos):
                        pass
                    elif restart_rect.collidepoint(event.pos):
                        game_start(screen)
                        board.screen.fill(bg_color)
                        board.draw()
                        display_numbers(screen)
                        game_in_progress_buttons(screen)
                    elif exit_rect.collidepoint(event.pos):
                        exit()

                    prev_clicked_cell = clicked_cell

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        value = 1
                        board.sketch(value)
                    if event.key == pygame.K_2:
                        value = 2
                        board.sketch(value)
                    if event.key == pygame.K_3:
                        value = 3
                        board.sketch(value)
                    if event.key == pygame.K_4:
                        value = 4
                        board.sketch(value)
                    if event.key == pygame.K_5:
                        value = 5
                        board.sketch(value)
                    if event.key == pygame.K_6:
                        value = 6
                        board.sketch(value)
                    if event.key == pygame.K_7:
                        value = 7
                        board.sketch(value)
                    if event.key == pygame.K_8:
                        value = 8
                        board.sketch(value)
                    if event.key == pygame.K_9:
                        value = 9
                        board.sketch(value)
                    if (event.key == pygame.K_KP_ENTER) and (value is not None):
                        board.place_number(value)
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()

            pygame.display.update()


def display_numbers(screen):
    array = generate_sudoku(9, removed_cells)
    puzzle_num_font = pygame.font.Font(None, 70)

    row_1 = array[0][:]
    for number in row_1:
        string_number = str(number)
        if number == 0:
            pass
        else:
            surf_number = puzzle_num_font.render(string_number, 0, line_color)  # text
            next = row_1.index(number) * 70
            surf_number_rect = surf_number.get_rect(center=((width // 9 - 35) + next, height // 9 - 40)) # position
            screen.blit(surf_number, surf_number_rect)

    row_2 = array[1][:]
    for number in row_2:
        string_number = str(number)
        if number == 0:
            pass
        else:
            surf_number = puzzle_num_font.render(string_number, 0, line_color)  # text
            next = row_2.index(number) * 70
            surf_number_rect = surf_number.get_rect(center=((width // 9 - 35) + next, height // 9 + 35)) # position
            screen.blit(surf_number, surf_number_rect)

    row_3 = array[2][:]
    for number in row_3:
        string_number = str(number)
        if number == 0:
            pass
        else:
            surf_number = puzzle_num_font.render(string_number, 0, line_color)  # text
            next = row_3.index(number) * 70
            surf_number_rect = surf_number.get_rect(center=((width // 9 - 35) + next, height // 9 + 100)) # position
            screen.blit(surf_number, surf_number_rect)

    row_4 = array[3][:]
    for number in row_4:
        string_number = str(number)
        if number == 0:
            pass
        else:
            surf_number = puzzle_num_font.render(string_number, 0, line_color)  # text
            next = row_4.index(number) * 70
            surf_number_rect = surf_number.get_rect(center=((width // 9 - 35) + next, height // 9 + 175)) # position
            screen.blit(surf_number, surf_number_rect)

    row_5 = array[4][:]
    for number in row_5:
        string_number = str(number)
        if number == 0:
            pass
        else:
            surf_number = puzzle_num_font.render(string_number, 0, line_color)  # text
            next = row_5.index(number) * 70
            surf_number_rect = surf_number.get_rect(center=((width // 9 - 35) + next, height // 9 + 240)) # position
            screen.blit(surf_number, surf_number_rect)

    row_6 = array[5][:]
    for number in row_6:
        string_number = str(number)
        if number == 0:
            pass
        else:
            surf_number = puzzle_num_font.render(string_number, 0, line_color)  # text
            next = row_6.index(number) * 70
            surf_number_rect = surf_number.get_rect(center=((width // 9 - 35) + next, height // 9 + 310)) # position
            screen.blit(surf_number, surf_number_rect)

    row_7 = array[6][:]
    for number in row_7:
        string_number = str(number)
        if number == 0:
            pass
        else:
            surf_number = puzzle_num_font.render(string_number, 0, line_color)  # text
            next = row_7.index(number) * 70
            surf_number_rect = surf_number.get_rect(center=((width // 9 - 35) + next, height // 9 + 385)) # position
            screen.blit(surf_number, surf_number_rect)

    row_8 = array[7][:]
    for number in row_8:
        string_number = str(number)
        if number == 0:
            pass
        else:
            surf_number = puzzle_num_font.render(string_number, 0, line_color)  # text
            next = row_8.index(number) * 70
            surf_number_rect = surf_number.get_rect(center=((width // 9 - 35) + next, height // 9 + 450)) # position
            screen.blit(surf_number, surf_number_rect)

    row_9 = array[8][:]
    for number in row_9:
        string_number = str(number)
        if number == 0:
            pass
        else:
            surf_number = puzzle_num_font.render(string_number, 0, line_color)  # text
            next = row_9.index(number) * 70
            surf_number_rect = surf_number.get_rect(center=((width // 9 - 35) + next, height // 9 + 520)) # position
            screen.blit(surf_number, surf_number_rect)

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
                    game_start(screen)
                    board.screen.fill(bg_color)
                    board.draw()
                    game_in_progress_buttons(screen)


        pygame.display.update()


# Main function
def main():
    game_start(screen)
    board.screen.fill(bg_color)
    board.draw()
    display_numbers(screen)
    game_in_progress_buttons(screen)


    """
    if the board is full and all the numbers match the solution:
        game_won(screen)
    elif the board is full and the numbers don't match the solution:
        game_over(screen)
    """

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # removes error message when window is closed by stopping while True loop

        pygame.display.update()


if __name__ == '__main__':
    main()

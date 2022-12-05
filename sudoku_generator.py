import math,random
import pygame
from constants import *

class SudokuGenerator:
    '''
	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = self.get_board()
        self.box_length = math.sqrt(row_length)

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return [[0 for row in range(self.row_length)] for column in range(self.row_length)] # row_length used twice because row will always be 9

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        pass

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        for space in self.board[row]:
            if space == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        for space in range(self.board):
            if self.board[space][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        i = row_start
        j = col_start
        while i < row_start + 3:
            while j < col_start + 3:
                if self.board[i][j] == num:
                    return False
                j += 1
            i += 1
            j = col_start
        return True 

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num):
            return True
        return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        digits_for_use = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        i = row_start
        j = col_start
        while i < row_start + 3:
            while j < col_start + 3:
                number = random.randint(1, 9)
                if number in digits_for_use:
                    number = random.randint(1, 9)
                else:
                    self.board[i][j] = number
                    digits_for_use.remove(number)
                j += 1
            i += 1
            j = col_start

    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        cells_to_remove = 64  # research: sudoku must have 17 clues to have a valid solution
        for cell in range(cells_to_remove):
            # pick random cell
            i = random.randint(0, 8)
            j = random.randint(0, 8)

            if self.board[i][j] == 0:  # if the cell is already zero:
                continue               # move on to the next cell
            else:                      # otherwise:
                self.board[i][j] = 0   # set that cell equal to zero

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


# recommended class
class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        pass


# recommended class
class Board:

    def __init__(self, width, height, screen, row, col, difficulty):
        # Constructor
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = self.initialize_board()
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(col)] for i in range(row)]
    def initialize_board(self):
        return [[0 for i in range(9)] for j in range(9)]
    def draw(self):
        # Thicker lines - Horizontal
        pygame.draw.line(self.screen, line_color, (0, square_width), (self.width, square_width), thick_line_width)
        pygame.draw.line(self.screen, line_color, (0, square_width * 2), (self.width, square_width * 2), thick_line_width)

        # Thicker lines - Vertical
        pygame.draw.line(self.screen, line_color, (square_width, 0), (square_width, self.width), thick_line_width)
        pygame.draw.line(self.screen, line_color, (square_width * 2, 0), (square_width * 2, self.width), thick_line_width)

        # Thinner lines - Horizontal
        pygame.draw.line(self.screen, line_color, (0, cell_width), (self.width, cell_width), thin_line_width)
        pygame.draw.line(self.screen, line_color, (0, cell_width * 2), (self.width, cell_width * 2), thin_line_width)
        pygame.draw.line(self.screen, line_color, (0, cell_width * 4), (self.width, cell_width * 4), thin_line_width)
        pygame.draw.line(self.screen, line_color, (0, cell_width * 5), (self.width, cell_width * 5), thin_line_width)
        pygame.draw.line(self.screen, line_color, (0, cell_width * 7), (self.width, cell_width * 7), thin_line_width)
        pygame.draw.line(self.screen, line_color, (0, cell_width * 8), (self.width, cell_width * 8), thin_line_width)

        # Thinner lines - Vertical
        pygame.draw.line(self.screen, line_color, (cell_width, 0), (cell_width, self.width), thin_line_width)
        pygame.draw.line(self.screen, line_color, (cell_width * 2, 0), (cell_width * 2, self.width), thin_line_width)
        pygame.draw.line(self.screen, line_color, (cell_width * 4, 0), (cell_width * 4, self.width), thin_line_width)
        pygame.draw.line(self.screen, line_color, (cell_width * 5, 0), (cell_width * 5, self.width), thin_line_width)
        pygame.draw.line(self.screen, line_color, (cell_width * 7, 0), (cell_width * 7, self.width), thin_line_width)
        pygame.draw.line(self.screen, line_color, (cell_width * 8, 0), (cell_width * 8, self.width), thin_line_width)

    def select(self, row, col):
        # Draws red border around selected cell
        pygame.draw.line(self.screen, outline_color, (col * cell_width, row * cell_width), ((col * cell_width) + cell_width, row * cell_width), thin_line_width)
        pygame.draw.line(self.screen, outline_color, (col * cell_width, (row * cell_width) + cell_width), ((col * cell_width) + cell_width, (row * cell_width) + cell_width), thin_line_width)
        pygame.draw.line(self.screen, outline_color, (col * cell_width, row * cell_width), (col * cell_width, (row * cell_width) + cell_width), thin_line_width)
        pygame.draw.line(self.screen, outline_color, ((col * cell_width) + cell_width, row * cell_width), ((col * cell_width) + cell_width, (row * cell_width) + cell_width), thin_line_width)

    def click(self, x, y):
        if y > 630:
            row = None
            col = None
        else:
            row = y // cell_width
            col = x // cell_width

        return row, col

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        if self.find_empty() is None:
            return True
        else:
            return False

    def update_board(self):
        self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(self.col)] for i in range(self.row)]

    def find_empty(self):
        pass

    def check_board(self):
        pass


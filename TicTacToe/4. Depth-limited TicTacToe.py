import pygame
import sys
from collections import deque

# Define colors
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)

# Initialize pygame
pygame.init()

# Set up the game window
WINDOW_SIZE = (400, 450)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe")

# Set up the game board
BOARD_SIZE = 3
board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Set up the fonts
score_font = pygame.font.Font(None, 30)
reset_font = pygame.font.Font(None, 24)

# Variable to keep track of the current player's turn
turn = "X"

# Variables to keep track of player scores
score_X = 0
score_O = 0

# Function to draw the score panel and reset button
def draw_score_panel():
    score_panel_rect = pygame.Rect(0, 0, WINDOW_SIZE[0], 40)
    pygame.draw.rect(screen, PURPLE, score_panel_rect)

    score_text = score_font.render(f"Player X: {score_X}   Player O: {score_O}", True, WHITE)
    screen.blit(score_text, (10, 5))

    reset_button_rect = pygame.Rect(WINDOW_SIZE[0] - 90, 5, 80, 30)
    pygame.draw.rect(screen, YELLOW, reset_button_rect)
    reset_text = reset_font.render("Reset", True, PURPLE)
    screen.blit(reset_text, (WINDOW_SIZE[0] - 75, 12))

# Function to draw the game board
def draw_board():
    screen.fill(PURPLE)
    draw_grid()

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == "X":
                draw_star(col * WINDOW_SIZE[0] // BOARD_SIZE, row * WINDOW_SIZE[1] // BOARD_SIZE)
            elif board[row][col] == "O":
                draw_o(col * WINDOW_SIZE[0] // BOARD_SIZE, row * WINDOW_SIZE[1] // BOARD_SIZE)

# Function to draw the grid lines
def draw_grid():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, WHITE, (i * WINDOW_SIZE[0] // BOARD_SIZE, 0), (i * WINDOW_SIZE[0] // BOARD_SIZE, WINDOW_SIZE[1]), 3)
        pygame.draw.line(screen, WHITE, (0, i * WINDOW_SIZE[1] // BOARD_SIZE), (WINDOW_SIZE[0], i * WINDOW_SIZE[1] // BOARD_SIZE), 3)

# Function to draw the "X" symbol
def draw_star(x, y):
    x_center = x + WINDOW_SIZE[0] // (2 * BOARD_SIZE)
    y_center = y + WINDOW_SIZE[1] // (2 * BOARD_SIZE)
    radius = WINDOW_SIZE[0] // (4 * BOARD_SIZE)

    pygame.draw.line(screen, WHITE, (x_center - radius, y_center), (x_center + radius, y_center), 5)
    pygame.draw.line(screen, WHITE, (x_center, y_center - radius), (x_center, y_center + radius), 5)
    pygame.draw.line(screen, WHITE, (x_center - radius, y_center - radius), (x_center + radius, y_center + radius), 5)
    pygame.draw.line(screen, WHITE, (x_center - radius, y_center + radius), (x_center + radius, y_center - radius), 5)

# Function to draw the "O" symbol
def draw_o(x, y):
    radius = WINDOW_SIZE[0] // (2 * BOARD_SIZE) - 5
    center_x = x + WINDOW_SIZE[0] // (2 * BOARD_SIZE)
    center_y = y + WINDOW_SIZE[1] // (2 * BOARD_SIZE)
    pygame.draw.circle(screen, WHITE, (center_x, center_y), radius, 3)

# Function to check for a win
def check_win(board, player):
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)):
            return True
        if all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True
    return False

# Function to check for a tie
def check_tie(board):
    return all(board[i][j] != "" for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

# Function to reset the game
def reset_game():
    global board, turn
    board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    turn = "X"
    draw_board()
    draw_score_panel()
    pygame.display.flip()

DEPTH_LIMIT = 2

def computer_move_dls():
    empty_cells = [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if board[i][j] == ""]
    
    if empty_cells:
        best_move = None
        best_score = float('-inf')

        for cell in empty_cells:
            row, col = cell
            board[row][col] = "O"
            score = minimax_dls(board, 0, False)
            board[row][col] = ""  # Reset the cell

            if score > best_score:
                best_score = score
                best_move = (row, col)

        if best_move:
            row, col = best_move
            board[row][col] = "O"

def minimax_dls(board, depth, is_maximizing):
    if depth == DEPTH_LIMIT:
        return 0  # Apply a heuristic evaluation at the depth limit
    
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if check_tie(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == "":
                    board[i][j] = "O"
                    score = minimax_dls(board, depth + 1, False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == "":
                    board[i][j] = "X"
                    score = minimax_dls(board, depth + 1, True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

def main():
    global turn, score_X, score_O
    computer_turn = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                col = x // (WINDOW_SIZE[0] // BOARD_SIZE)
                row = y // (WINDOW_SIZE[1] // BOARD_SIZE)

                if board[row][col] == "" and turn == "X" and not computer_turn:
                    board[row][col] = "X"

                    if check_win(board, "X"):
                        score_X += 1
                        winner_text = score_font.render("Player X wins!", True, WHITE)
                        screen.blit(winner_text, (40, WINDOW_SIZE[1] // 2))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        reset_game()
                    elif check_tie(board):
                        tie_text = score_font.render("It's a tie!", True, WHITE)
                        screen.blit(tie_text, (120, WINDOW_SIZE[1] // 2))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        reset_game()
                    else:
                        turn = "O"
                        computer_turn = True

        if computer_turn and turn == "O":
            computer_move_dls()
            computer_turn = False

            if check_win(board, "O"):
                score_O += 1
                winner_text = score_font.render("Player O wins!", True, WHITE)
                screen.blit(winner_text, (40, WINDOW_SIZE[1] // 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                reset_game()
            elif check_tie(board):
                tie_text = score_font.render("It's a tie!", True, WHITE)
                screen.blit(tie_text, (120, WINDOW_SIZE[1] // 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                reset_game()
            else:
                turn = "X"

        draw_board()
        draw_score_panel()
        pygame.display.flip()

if __name__ == "__main__":
    draw_board()
    draw_score_panel()
    main()

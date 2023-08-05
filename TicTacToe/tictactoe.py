import pygame
import sys

# Define colors
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)

# Initialize pygame
pygame.init()

# Set up the game window
WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe")

# Set up the game board
BOARD_SIZE = 3
board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Set up the fonts
font = pygame.font.Font(None, 60)

# Variable to keep track of the current player's turn
turn = "X"

def draw_grid():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, WHITE, (i * WINDOW_SIZE[0] // BOARD_SIZE, 0), (i * WINDOW_SIZE[0] // BOARD_SIZE, WINDOW_SIZE[1]), 3)
        pygame.draw.line(screen, WHITE, (0, i * WINDOW_SIZE[1] // BOARD_SIZE), (WINDOW_SIZE[0], i * WINDOW_SIZE[1] // BOARD_SIZE), 3)

def draw_star(x, y):
    x_center = x + WINDOW_SIZE[0] // (2 * BOARD_SIZE)
    y_center = y + WINDOW_SIZE[1] // (2 * BOARD_SIZE)
    radius = WINDOW_SIZE[0] // (4 * BOARD_SIZE)

    pygame.draw.line(screen, WHITE, (x_center - radius, y_center), (x_center + radius, y_center), 5)
    pygame.draw.line(screen, WHITE, (x_center, y_center - radius), (x_center, y_center + radius), 5)
    pygame.draw.line(screen, WHITE, (x_center - radius, y_center - radius), (x_center + radius, y_center + radius), 5)
    pygame.draw.line(screen, WHITE, (x_center - radius, y_center + radius), (x_center + radius, y_center - radius), 5)

def draw_o(x, y):
    radius = WINDOW_SIZE[0] // (2 * BOARD_SIZE) - 5
    center_x = x + WINDOW_SIZE[0] // (2 * BOARD_SIZE)
    center_y = y + WINDOW_SIZE[1] // (2 * BOARD_SIZE)
    pygame.draw.circle(screen, WHITE, (center_x, center_y), radius, 3)

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

def check_tie(board):
    return all(board[i][j] != "" for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

def draw_board():
    screen.fill(PURPLE)
    draw_grid()

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == "X":
                draw_star(col * WINDOW_SIZE[0] // BOARD_SIZE, row * WINDOW_SIZE[1] // BOARD_SIZE)
            elif board[row][col] == "O":
                draw_o(col * WINDOW_SIZE[0] // BOARD_SIZE, row * WINDOW_SIZE[1] // BOARD_SIZE)

    pygame.display.flip()

def main():
    global turn
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                col = x // (WINDOW_SIZE[0] // BOARD_SIZE)
                row = y // (WINDOW_SIZE[1] // BOARD_SIZE)
                if board[row][col] == "":
                    if turn == "X":
                        board[row][col] = "X"
                    else:
                        board[row][col] = "O"

                    if check_win(board, turn):
                        winner_text = font.render(f"Player {turn} wins!", True, WHITE)
                        screen.blit(winner_text, (40, WINDOW_SIZE[1] // 2))
                        pygame.display.flip()
                        pygame.time.wait(2000)  # Pause for 2 seconds
                        pygame.quit()
                        sys.exit()

                    if check_tie(board):
                        tie_text = font.render("It's a tie!", True, WHITE)
                        screen.blit(tie_text, (120, WINDOW_SIZE[1] // 2))
                        pygame.display.flip()
                        pygame.time.wait(2000)  # Pause for 2 seconds
                        pygame.quit()
                        sys.exit()

                    turn = "X" if turn == "O" else "O"

        # Redraw the board
        draw_board()

if __name__ == "__main__":
    draw_board()  # Draw the initial board
    main()

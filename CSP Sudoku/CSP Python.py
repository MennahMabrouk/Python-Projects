import tkinter as tk
import time
from itertools import product

def is_valid_move(puzzle, row, col, num):
    if num in puzzle[row] or num in [puzzle[i][col] for i in range(9)]:
        return False

    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if puzzle[i][j] == num:
                return False

    return True

def solve_sudoku_csp(puzzle):
    def solve(puzzle):
        for row, col in product(range(9), repeat=2):
            if puzzle[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(puzzle, row, col, num):
                        puzzle[row][col] = num
                        set_puzzle(puzzle)
                        app.update()
                        time.sleep(0.1)  # Adjust the delay time as desired
                        if solve(puzzle):
                            return True
                        puzzle[row][col] = 0
                return False
        return True

    if solve(puzzle):
        return puzzle
    return None

app = tk.Tk()
app.title("CSP Sudoku Solver")

sudoku_labels = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        label = tk.Label(app, width=4, height=2, relief="ridge", borderwidth=2)
        label.grid(row=i, column=j, padx=5, pady=5)
        label.config(font=("Arial", 16))
        sudoku_labels[i][j] = label

# Create bold borders for 3x3 subgrids
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        for x in range(3):
            for y in range(3):
                label = sudoku_labels[i + x][j + y]
                label.config(borderwidth=2 if x == 1 and y == 1 else 1)

def set_puzzle(puzzle):
    for i in range(9):
        for j in range(9):
            value = puzzle[i][j]
            label = sudoku_labels[i][j]
            if value == 0:
                label.config(text="", bg="white")
            else:
                label.config(text=str(value), bg="lightgray")

def clear_puzzle():
    for i in range(9):
        for j in range(9):
            label = sudoku_labels[i][j]
            label.config(text="", bg="white")

clear_button = tk.Button(app, text="Clear", command=clear_puzzle)
clear_button.grid(row=10, column=4, padx=5, pady=10)

solve_button = tk.Button(app, text="Solve CSP", command=lambda: solve_sudoku_csp(puzzle))
solve_button.grid(row=10, column=3, padx=5, pady=10)

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

set_puzzle(puzzle)

app.mainloop()

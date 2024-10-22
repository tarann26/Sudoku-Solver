# Sudoku Solver 

This repository contains two Python scripts: a **Sudoku Solver** and a **Graphical User Interface (GUI)** for playing and solving Sudoku puzzles. The solver script can handle puzzles of varying difficulties, and the GUI allows users to interact with Sudoku puzzles through a visual interface.

## Table of Contents
- [Files](#files)
- [Features](#features)
- [Project Structure](#Project-Structure)
- [Classes Overview](#Classes-Overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies](#technologies)

## Files

This project provides a Sudoku puzzle generator and solver with a graphical user interface (GUI) implemented using **Pygame**. It includes the following components:
- `solver.py`: A Python script implementing a Sudoku solver by implementing a backtracking algorithm.
- `gui.py`: A Python script implementing a GUI for Sudoku, which handles the generation, display, and user interaction with the Sudoku grid.


## Features

- **Sudoku Puzzle Generation**: The `Grid` class generates random, playable Sudoku puzzles with three levels of difficulty.
- **GUI for Sudoku**: The GUI built using **Pygame** allows users to interact with the puzzle, input numbers, and visualize the solving process.
- **Backtracking Algorithm**: The `SudokuSolver` class uses a backtracking algorithm to solve the puzzle and is integrated with the `Grid` class.

## Project Structure

- **GUI.py**: Contains the main `Grid` class and handles all GUI-related functions, including drawing the grid, allowing user interaction, and invoking the solver.
- **solver.py**: Contains the `SudokuSolver` class which provides a backtracking-based Sudoku solver.
- **README.md**: The file you are currently reading.

## Classes Overview

### 1. `Grid` Class (in `GUI.py`)

The `Grid` class is responsible for:
- **Puzzle Generation**: Generates a random Sudoku puzzle on initialization.
- **Drawing the Grid**: Displays a 9x9 Sudoku grid with thick lines separating 3x3 subgrids.
- **User Interaction**: Allows users to select cells, input numbers, and solve the puzzle using the backtracking algorithm.
- **Solving the Puzzle**: Connects with the `SudokuSolver` to solve the grid and visually update the GUI.

#### Key Methods:
- `generate_sudoku()`: Generates a new Sudoku puzzle with random blank spaces.
- `place(val)`: Places a number in the selected cell, validating the input.
- `solve_gui()`: Solves the puzzle visually, updating the GUI with each step.
- `is_finished()`: Checks if the puzzle is fully solved.

### 2. `SudokuSolver` Class (in `solver.py`)

The `SudokuSolver` class is a standalone backtracking solver that solves any valid Sudoku board. It takes a 2D list (9x9 grid) as input and uses recursion to find the solution.

#### Key Methods:
- `valid(num, pos)`: Checks if placing `num` in the given position `(row, col)` is valid.
- `find_empty()`: Finds the next empty cell (where the value is 0).
- `solve()`: Implements the backtracking algorithm to fill the board and solve the puzzle.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo-url.git
    cd your-repo-url
    ```

2. Install the required Python packages:
    ```bash
    pip install pygame
    pip install tkinter
    ```

## Usage

1. To run the **GUI** for playing Sudoku:
    ```bash
    python gui.py
    ```
2. To run the **Sudoku solver** script: press spacebar

### Running the Solver
- The `solver.py` script solves any valid Sudoku puzzle.
- You can input a puzzle as a 9x9 grid and receive the solution in the terminal.

### Running the GUI
- The `gui.py` script opens a Sudoku game window.

## Features

- **Sudoku Solver**:
  - Solves any valid 9x9 Sudoku puzzle.
  - Efficient algorithm to provide a quick solution.

- **Graphical Interface**:
  - Interactive Sudoku board using Pygame.
  - Option to solve the puzzle automatically.
  - Weighted randomness for generating puzzles of varying difficulties.

## Technologies

- **Python**: Core programming language for the logic and GUI.
- **Pygame**: Used for rendering the graphical interface for the Sudoku game.


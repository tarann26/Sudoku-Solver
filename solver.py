class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def valid(self, num, pos):
        row, col = pos

        # Check row
        for i in range(9):
            if self.grid[row][i] == num and col != i:
                return False

        # Check column
        for i in range(9):
            if self.grid[i][col] == num and row != i:
                return False

        # Check 3x3 box
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.grid[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return (i, j)  # row, col
        return None

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(i, (row, col)):
                self.grid[row][col] = i

                if self.solve():
                    return True

                self.grid[row][col] = 0  # backtrack

        return False

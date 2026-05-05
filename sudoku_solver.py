def print_grid(grid):
    print("+-------+-------+-------+")
    for i, row in enumerate(grid):
        if i in (3, 6):
            print("+-------+-------+-------+")
        line = "| "
        for j, val in enumerate(row):
            line += (str(val) if val != 0 else ".") + " "
            if j in (2, 5):
                line += "| "
        print(line + "|")
    print("+-------+-------+-------+")
def is_valid(grid, row, col, num):
    # Check row
    if num in grid[row]:
        return False
    if num in [grid[r][col] for r in range(9)]:
        return False
    box_r, box_c = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if grid[r][c] == num:
                return False
    return True
def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True
def get_puzzle_from_user():
    print("Enter your Sudoku puzzle row by row.")
    print("Use 0 or '.' for empty cells. Separate digits with spaces.")
    print("Example row:  5 3 0 0 7 0 0 0 0\n")
    grid = []
    for i in range(1, 10):
        while True:
            raw = input(f"Row {i}: ").strip().replace(".", "0").split()
            if len(raw) == 9 and all(d.isdigit() and 0 <= int(d) <= 9 for d in raw):
                grid.append([int(d) for d in raw])
                break
            print("  ⚠ Invalid input. Enter exactly 9 digits (0-9).")
    return grid
def main():
    print("=" * 45)
    print("           SUDOKU SOLVER")
    print("=" * 45)
    print("Options:")
    print("  1. Solve a sample puzzle")
    print("  2. Enter your own puzzle")
    print("-" * 45)
    choice = input("Choose (1/2): ").strip()
    if choice == "1":
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
    else:
        grid = get_puzzle_from_user()
    print("\nUnsolved Puzzle:")
    print_grid(grid)
    print("\nSolving...")
    if solve(grid):
        print("\n✅ Solved Puzzle:")
        print_grid(grid)
    else:
        print("\n❌ No solution exists for this puzzle.")
if __name__ == "__main__":
    main()

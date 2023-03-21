from typing import List


def read_txt_line_by_line(filename: str) -> List[List[int]]:
    """Reads a text file line by line and returns a list of lists of integers"""
    all_lines = []
    with open(filename) as f:
        for line in f:
            all_lines.append([int(i) for i in line.split()])
    return all_lines


def largest_product_in_grid(grid: List[List[int]], n: int) -> int:
    """Returns the largest product of n adjacent numbers in the same direction (up, down, left, right, or diagonally)
    in grid"""
    largest = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Check right
            if j + n <= len(grid[i]):
                product = 1
                for k in range(n):
                    product *= grid[i][j + k]
                if product > largest:
                    largest = product
            # Check down
            if i + n <= len(grid):
                product = 1
                for k in range(n):
                    product *= grid[i + k][j]
                if product > largest:
                    largest = product
            # Check down-right
            if i + n <= len(grid) and j + n <= len(grid[i]):
                product = 1
                for k in range(n):
                    product *= grid[i + k][j + k]
                if product > largest:
                    largest = product
            # Check down-left
            if i + n <= len(grid) and j - n >= 0:
                product = 1
                for k in range(n):
                    product *= grid[i + k][j - k]
                if product > largest:
                    largest = product
    return largest


if __name__ == "__main__":
    grid_txt = "grid.txt"
    # print(read_txt_line_by_line(grid_txt))
    print(largest_product_in_grid(read_txt_line_by_line(grid_txt), 4))

import itertools

f1 = open('input1.txt', 'r')
i1 = f1.read()
f1.close()
import re
sample = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

def sol1(input):
    grid = input.splitlines()
    rows, cols = len(grid), len(grid[0])
    result = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        count += 1
                if count < 4:
                    result.append((r, c))
    return len(result)


def iterate_directions(grid, rows, cols):
    removed = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        count += 1
                if count < 4:
                    grid[r][c] = "."
                    removed += 1
    return removed


def sol2(input):
    grid = input.splitlines()
    matrix =  [list(sub) for sub in grid]

    rows, cols = len(matrix), len(matrix[0])
    removed = 0
    new_removed = iterate_directions(matrix,rows,cols)
    while new_removed > 0:
        removed += new_removed
        new_removed = iterate_directions(matrix,rows,cols)
    return removed

print(sol2(i1))
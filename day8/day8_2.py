from termcolor import colored

with open('input.txt') as file:
    lines = file.read().strip()

grid = []
for row in lines.split('\n'):
    grid.append([int(d) for d in list(row)])

n, ans = len(grid), -1

def compute(i, j):
    w, x, y, z = 0, 0, 0, 0
    c = grid[i][j]
    for w in range(i + 1, n):
        if c <= grid[w][j]: break
    for x in range(i - 1, -1, -1):
        if c <= grid[x][j]: break
    for y in range(j + 1, n):
        if c <= grid[i][y]: break
    for z in range(j - 1, -1, -1):
        if c <= grid[i][z]: break
    w -= i; x = i - x; y -= j; z = j - z
    return w * x * y * z

for i in range(n):
    for j in range(n):
        ans = max(ans, compute(i, j))

print(ans)

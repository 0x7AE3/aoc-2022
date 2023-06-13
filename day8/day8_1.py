from termcolor import colored

with open('input.txt') as file:
    lines = file.read().strip()

grid = []
for row in lines.split('\n'):
    grid.append([int(d) for d in list(row)])

n, ans = len(grid), 0

def check(i, j):
    if i == 0 or j == 0 or i == n - 1 or j == n - 1:
        return True
    c = grid[i][j]
    for a in range(i + 1, n):
        if grid[a][j] >= c: break
        if a == n - 1: return True
    for a in range(i - 1, -1, -1):
        if grid[a][j] >= c: break
        if a == 0: return True
    for b in range(j + 1, n):
        if grid[i][b] >= c: break
        if b == n - 1: return True
    for b in range(j - 1, -1, -1):
        if grid[i][b] >= c: break
        if b == 0: return True
    return False

for i in range(n):
    for j in range(n):
        ans += check(i, j)
        if check(i, j):
        	print(colored(grid[i][j], 'red'), end = ' \n'[j == n - 1])
        else:
        	print(str(grid[i][j]), end = ' \n'[j == n - 1])

print(ans)

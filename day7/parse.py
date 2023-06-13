

ans = 0
folders = set()

with open('input.txt') as file:
    lines = file.read().strip().split('\n')
    for line in lines:
        if line.startswith('dir'):
            folders.add(line[4:])

print(folders, len(folders))
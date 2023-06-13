with open('input.txt') as file:
    lines = file.read().strip()

pwd = []
files, folders, sizes = dict(), set(), dict()

for command in lines.split('\n'):
    if command == '$ cd /':
        pwd = []
    elif command == '$ cd ..':
        pwd.pop()
    elif command.startswith('$ cd'):
        pwd.append(command[5:])
    elif command == '$ ls':
        continue
    else:
        size, name = command.split(' ')
        if size == 'dir':
            continue
        files['/'.join(pwd + [name])] = int(size)
    folders.add('/'.join(pwd))

for folder in folders:
	size = sum(files[file] for file in files if file.startswith(folder))
	sizes[folder] = size

print(min([size for size in sizes.values() if 70000000 - sizes[''] + size >= 30000000]))

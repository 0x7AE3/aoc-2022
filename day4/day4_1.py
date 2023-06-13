ans = 0

with open('input.txt') as file:
    for line in file.readlines():
        if line == '\n': break

        a = int(line.split('-')[0])
        b = int(line.split('-')[1].split(',')[0])
        c = int(line.split(',')[1].split('-')[0])
        d = int(line.split(',')[1].split('-')[1])

        ans += ((a <= c and d <= b) or (a >= c and d >= b))

print(ans)

with open('input.txt') as file:
    lines = file.read().strip().split('\n')

dd = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]

h, t = [0, 0], [0, 0]
vis = set()

for line in lines:
    d, n = line[0], int(line[2:])
    match d:
        case 'R':
            for _ in range(n):
                print(h, t)
                h[0] += 1
                # if h[0] - t[0] == 2: t[0] += 1 
                nxt = True in [(h[0] + x == t[0] and h[1] + y == t[1]) for (x, y) in dd]
                t[0] += not nxt
                vis.add(tuple(t))
        case 'L':
            for _ in range(n):
                print(h, t)
                h[0] -= 1
                nxt = True in [(h[0] + x == t[0] and h[1] + y == t[1]) for (x, y) in dd]
                t[0] += not nxt
                vis.add(tuple(t))
        case 'U':
            for _ in range(n):
                print(h, t)
                h[1] += 1
                nxt = True in [(h[0] + x == t[0] and h[1] + y == t[1]) for (x, y) in dd]
                t[1] += not nxt
                vis.add(tuple(t))
        case 'D':
            for _ in range(n):
                print(h, t)
                h[1] -= 1
                nxt = True in [(h[0] + x == t[0] and h[1] + y == t[1]) for (x, y) in dd]
                t[1] -= not nxt
                vis.add(tuple(t))
# print(vis)
print(len(vis))

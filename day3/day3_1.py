ans = 0

with open('input.txt') as file:
    data = file.read().strip().split('\n')
    for rns in data:
        half = len(rns) // 2
        common = ord(set(rns[:half]).intersection(rns[half:]).pop())
        if ((common - ord('A')) < 26): ans += (common - ord('A') + 1 + 26)
        else: ans += (common - ord('a') + 1)

print(ans)

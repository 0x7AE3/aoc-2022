ans = 0

with open('input.txt') as file:
    data = file.read().strip().split('\n')
    for i in range(0, len(data), 3):
        group = [data[i], data[i + 1], data[i + 2]]
        common = ord(set(data[i]).intersection(set(data[i + 1])) \
                .intersection(set(data[i + 2])).pop())
        if ((common - ord('A')) < 26): ans += (common - ord('A') + 1 + 26)
        else: ans += (common - ord('a') + 1)

print(ans)

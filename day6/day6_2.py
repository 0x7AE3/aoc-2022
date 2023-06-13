with open('input.txt') as file:
    data = file.read().strip()
ans = 0
while len(set([data[i] for i in range(ans, ans + 14)])) != 14: ans += 1
print(ans + 14)

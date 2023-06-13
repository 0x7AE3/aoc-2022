with open('input.txt') as file:
    data = file.read().strip()
ans = 0
while len(set([data[ans], data[ans + 1], data[ans + 2], data[ans + 3]])) != 4: ans += 1
print(ans + 4)

points = {
    'A X' : 3,
    'A Y' : 4,
    'A Z' : 8,
    'B X' : 1,
    'B Y' : 5,
    'B Z' : 9,
    'C X' : 2,
    'C Y' : 6,
    'C Z' : 7
} 

ans = 0
with open('input.txt') as file:
    print(sum([points[line] for line in file.read().split('\n')[:-1]]))

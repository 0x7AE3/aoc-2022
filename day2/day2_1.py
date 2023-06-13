points = {
    'A X' : 4,
    'A Y' : 8,
    'A Z' : 3,
    'B X' : 1,
    'B Y' : 5,
    'B Z' : 9,
    'C X' : 7,
    'C Y' : 2,
    'C Z' : 6
} 

ans = 0
with open('input.txt') as file:
    print(sum([points[line] for line in file.read().split('\n')[:-1]]))

maxes = [-1, -2, -3]

with open('input.txt') as file:
   lines = file.readlines()
   temp = 0

   for line in lines:
       if line == '\n':
           if temp > maxes[0]: maxes = [temp, maxes[0], maxes[1]]
           elif temp > maxes[1]: maxes = [maxes[0], temp, maxes[1]]
           elif temp > maxes[2]: maxes = [maxes[0], maxes[1], temp]
           temp = 0
           continue
       temp += int(line)

print(sum(maxes))

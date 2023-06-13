ans = -1

with open('input.txt') as file:
   lines = file.readlines()
   temp = 0
   for line in lines:
       if line == '\n':
           ans = max(ans, temp)
           temp = 0
           continue
       temp += int(line)

print(ans)

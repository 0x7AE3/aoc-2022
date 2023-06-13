stacks = [[] for _ in range(9 + 1)]

with open('input.txt') as file:

    lines, line_num = file.readlines(), 0
    for line in lines:
        if line[1] == '1': break
        for i in range(1, 9 + 1):
            if line[4*i - 3] != ' ':
                stacks[i].append(line[4*i - 3])
        line_num += 1

    stacks = [stack[::-1] for stack in stacks]

    for line in lines[line_num+2:]:
        split = line.split(" ")
        count, start, end = int(split[1]), int(split[3]), int(split[5])

        stacks[end] += stacks[start][-count:][::-1]
        stacks[start] = stacks[start][:-count]

print(''.join(['' if not stack else str(stack[-1]) for stack in stacks]))

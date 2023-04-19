import re

with open('../data/input_5.txt') as f:
    data = f.read().split("\n\n")
    boxes = data[0]
    instructions = data[1].split("\n")

    # read boxes in to list of lists
    lines = boxes.split("\n")
    stacks = [[] for i in range(9)]  # or use {i: [] for i in range(1, 10)} - but then can't print in order
    char = 1
    n = 0
    for line in lines:
        while char < len(line):
            if line[char] != " " and not line[char].isnumeric():
                stacks[n].append(line[char])
            char += 4
            n += 1
        char = 1
        n = 0

    for stack in stacks:
        stack.reverse()  # order from bottom to top box

# part A
# for line in instructions:
#     moves = int(re.search(r'move (.*?) from', line).group(1))
#     start = int(re.search(r'from (.*?) to', line).group(1)) - 1  # list 0 indexed (use dict instead)
#     end = int(line[-1]) - 1  # should use regex
#
#     for i in range(moves):
#         box = stacks[start].pop()
#         stacks[end].append(box)
#
# for stack in stacks:
#     print(stack[-1], end="")  # print top boxes in each stack


# # part B
for line in instructions:
    num_boxes = int(re.search(r'move (.*?) from', line).group(1))
    start = int(re.search(r'from (.*?) to', line).group(1)) - 1  # list 0 indexed
    end = int(line[-1]) - 1

    boxes_to_move = stacks[start][-num_boxes:]
    stacks[start] = stacks[start][:-num_boxes]
    stacks[end] = stacks[end] + boxes_to_move

for stack in stacks:
    print(stack[-1], end="")

# can only run one part at a time

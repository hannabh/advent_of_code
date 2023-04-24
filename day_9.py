with open("../data/input_9.txt") as f:
    instructions = f.read().splitlines()


def move_head(head_pos, direction):
    if direction == "R":
        head_pos[0] += 1
    if direction == "L":
        head_pos[0] -= 1
    if direction == "U":
        head_pos[1] += 1
    if direction == "D":
        head_pos[1] -= 1
    return head_pos


def move_tail(head_pos, tail_pos):
    diff_x = tail_pos[0] - head_pos[0]
    diff_y = tail_pos[1] - head_pos[1]

    if abs(diff_x) <= 1 and abs(diff_y) <= 1:
        return tail_pos
    else:
        if diff_x >= 1:
            tail_pos[0] -= 1
        if diff_x <= -1:
            tail_pos[0] += 1
        if diff_y >= 1:
            tail_pos[1] -= 1
        if diff_y <= -1:
            tail_pos[1] += 1
    return tail_pos


# Part A
head = [0, 0]
tail = [0, 0]
tail_positions = [[0, 0]]

for line in instructions:
    direction = line.split()[0]
    steps = int(line.split()[1])
    for i in range(steps):
        head = move_head(head, direction)
        tail = move_tail(head, tail)

        temp = tail.copy()  # see example!
        if tail not in tail_positions:
            tail_positions.append(temp)

print(len(tail_positions))

# Part B
rope = [[0, 0] for i in range(10)]  # head = rope[0], tail = rope[9]
tail_positions = [[0, 0]]

for line in instructions:
    direction = line.split()[0]
    steps = int(line.split()[1])
    for i in range(steps):
        rope[0] = move_head(rope[0], direction)
        for j in range(1, 10):
            rope[j] = move_tail(rope[j-1], rope[j])

        temp = rope[9].copy()
        if temp not in tail_positions:
            tail_positions.append(temp)

print(len(tail_positions))

# example of loop issue - doesn't work, need copy()
'''
tail = [0, 0]
positions_visited = [[0, 0]]
for i in range(3):
    print(positions_visited)
    tail[1] += 1
    print("tail:", tail)
    print(positions_visited, "\n")  # here positions_visited has changed
    positions_visited.append(tail)
'''

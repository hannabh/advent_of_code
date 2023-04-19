with open('../data/input_1.txt') as f:
    lines = f.read().splitlines()  # list of lines in file, without \n. Same as f.read().split("\n")

    elves = []
    calorie_count = 0
    for line in lines:
        if line == "":
            elves.append(calorie_count)
            calorie_count = 0
        else:
            calorie_count += int(line)

    print(max(elves))

    elves.sort()
    print(sum(elves[-3:]))

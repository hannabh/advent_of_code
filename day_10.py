with open('../data/input_10.txt') as f:
    input = f.read().splitlines()


# Part 1
x = 1
cycle = 1
signal_strengths = {}
for line in input:
    if line == "noop":
        signal_strengths[cycle] = cycle * x
        cycle += 1
    elif line.startswith("addx"):
        increment = int(line.split(" ")[1])
        signal_strengths[cycle] = cycle * x
        cycle += 1
        signal_strengths[cycle] = cycle * x
        x += increment
        cycle += 1

to_check = [20, 60, 100, 140, 180, 220]
sum = 0
for val in to_check:
    sum += signal_strengths[val]
print(sum)


# Part 2
cycle = 1
x = 1  # x position of sprite center
pixel = 0


def draw_pixel(cycle, x, pixel):
    pixel_x = pixel % 40
    if abs(x - pixel_x) <= 1:
        print("#", end="")
    else:
        print(".", end="")
    if cycle % 40 == 0:
        print("\n", end="")
    return x


for line in input:
    if line == "noop":
        x = draw_pixel(cycle, x, pixel)
        cycle += 1
        pixel += 1
    elif line.startswith("addx"):
        increment = int(line.split(" ")[1])
        x = draw_pixel(cycle, x, pixel)
        cycle += 1
        pixel += 1

        x = draw_pixel(cycle, x, pixel)
        x += increment
        cycle += 1
        pixel += 1

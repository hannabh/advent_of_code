with open('../data/input_3.txt') as f:
    rucksacks = f.read().splitlines()


def get_value(letter):
    if letter.isupper():
        value = ord(letter) - 38  # ord() gives ASCII value
    else:
        value = ord(letter) - 96
    return value


value_sum = 0
for rucksack in rucksacks:
    if rucksack != "":
        comp_1 = rucksack[:int(len(rucksack) / 2)]
        comp_2 = rucksack[int(len(rucksack) / 2):]
        letter = list(set(comp_1) & set(comp_2))[0]
        value_sum += get_value(letter)

print("Part A: ", value_sum)

value_sum = 0
n = 0
while n < len(rucksacks):
    if rucksacks[n] != "":
        letter = list(set(rucksacks[n]) & set(rucksacks[n+1]) & set(rucksacks[n+2]))[0]
        value_sum += get_value(letter)
    n += 3

print("Part B: ", value_sum)

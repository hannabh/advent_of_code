with open('../data/input_4.txt') as f:
    assignments = f.read().splitlines()


def get_section_list(assignment):
    return list(range(int(assignment.split("-")[0]), int(assignment.split("-")[1]) + 1))


full_overlap = 0
partial_overlap = 0
for a in assignments:
    a = a.split(",")
    elf1 = set(get_section_list(a[0]))
    elf2 = set(get_section_list(a[1]))
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        full_overlap += 1
    if len(elf1.intersection(elf2)) > 0:
        partial_overlap += 1

print("Part A: ", full_overlap)
print("Part B: ", partial_overlap)

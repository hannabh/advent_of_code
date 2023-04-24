import numpy as np

data = open('../data/input_8.txt').read().splitlines()

forest = [[int(t) for t in row] for row in data]
forest = np.array(forest)
forest_transposed = forest.transpose()


# Part A
visible_trees = 0

for i in range(len(forest)):
    for j in range(len(forest[0])):
        tree_height = forest[i][j]
        if (
                all([x < tree_height for x in forest[i][:j]]) or
                all([x < tree_height for x in forest[i][j+1:]]) or
                all([x < tree_height for x in forest_transposed[j][:i]]) or
                all([x < tree_height for x in forest_transposed[j][i+1:]])
        ):
            visible_trees += 1

print(visible_trees)


# Part B
def get_view(tree_height, trees):
    viewing_distance = 0
    for t in trees:
        viewing_distance += 1
        if t >= tree_height:
            break
    return viewing_distance


max_score = 0
for i in range(len(forest)):
    for j in range(len(forest[0])):
        tree_height = forest[i][j]
        score_left = get_view(tree_height, forest[i][:j][::-1])
        score_right = get_view(tree_height, forest[i][j+1:])
        score_top = get_view(tree_height, forest_transposed[j][:i][::-1])
        score_bottom = get_view(tree_height, forest_transposed[j][i+1:])
        score = score_right * score_left * score_top * score_bottom
        if score > max_score:
            max_score = score

print(max_score)

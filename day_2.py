import pandas as pd

df = pd.read_csv("../data/input_2.txt", delimiter=" ", header=None, names=["opponent_code", "you_code"])


def choose_response(part, you, opponent):
    if part == 'a':
        response_dict = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
        return response_dict[you]
    elif part == 'b':
        response_dict = {
            'rock': ['scissors', 'rock', 'paper'],
            'paper': ['rock', 'paper', 'scissors'],
            'scissors': ['paper', 'scissors', 'rock']
        }
        # rows are opponent's move, columns are your instruction
        response_df = pd.DataFrame.from_dict(response_dict, orient='index', columns=['X', 'Y', 'Z'])
        return response_df[you][opponent]


def calc_points_play(you):
    points_play_dict = {'rock': 1, 'paper': 2, 'scissors': 3}
    return points_play_dict[you]


def calc_points_outcome(you, opponent):
    points_outcome = {
        'rock': [3, 6, 0],
        'paper': [0, 3, 6],
        'scissors': [6, 0, 3]
    }
    # rows are opponent's move, columns are your move
    # 0 points if you lost, 3 if the round was a draw, and 6 if you won
    points_outcome = pd.DataFrame.from_dict(points_outcome, orient='index', columns=['rock', 'paper', 'scissors'])
    return points_outcome[you][opponent]


def play_game(part):

    opponent_play_dict = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    df["opponent_play"] = df.apply(lambda row: opponent_play_dict[row["opponent_code"]], axis=1)

    df["you_play"] = df.apply(lambda row: choose_response(part, row["you_code"], row["opponent_play"]), axis=1)

    df["points_play"] = df.apply(lambda row: calc_points_play(row["you_play"]), axis=1)

    df["points_outcome"] = df.apply(lambda row:
                                    calc_points_outcome(row["you_play"], row["opponent_play"]), axis=1)

    df["points_total"] = df["points_play"] + df["points_outcome"]

    return df


df = play_game(part='b')
print("Points for game: ", sum(df["points_total"]))

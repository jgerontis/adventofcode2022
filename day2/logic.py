points = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
    1: 1,
    2: 2,
    3: 3,
}

def outcome(opp, you):
    # you draw
    if points[opp] == points[you]:
        return 3
    # you win
    if points[opp] - points[you] == -1 or points[opp] - points[you] == 2:
        return 6
    # you lose
    return 0

def points_per_round(opp, you):
    return points[you] + outcome(opp, you)

# This function made me feel clever
def calculate_move(opp, outcome):
    # lose
    if outcome == "X":
        return (points[opp] - 2) % 3 + 1
    # draw
    if outcome == "Y":
        return points[opp]
    # win
    return (points[opp] % 3) + 1

from logic import points_per_round, calculate_move

def main():
    fin = open("puzzle.txt", "r")
    part_one_score = 0
    part_two_score = 0
    for line in fin:
        line = line.strip().split(" ")
        part_one_score += points_per_round(line[0], line[1])
        part_two_score += points_per_round(line[0], calculate_move(line[0], line[1]))
    fin.close()
    print(part_one_score)
    print(part_two_score)

main()

from logic import *

def main():
    fin = open("puzzle.txt", "r")
    part_one_total = 0
    part_two_total = 0
    count = 0
    team = ["","",""]
    for line in fin:
        line = line.strip()
        part_one_total += item_priority(find_item(line))
        # part 2 stuff
        team[count] = line
        count += 1
        if count == 3:
            part_two_total += item_priority(find_badge_item(team))
            count = 0
    fin.close()
    print(part_one_total)
    print(part_two_total)

main()
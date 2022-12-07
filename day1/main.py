def main():
    # part 1
    fin = open("day1-input.txt","r")
    elves = []
    elf = 0
    for line in fin:
        if line != "\n":
            elf += int(line)
        else:
            elves.append(elf)
            print("appending elf")
            elf = 0
    fin.close()
    print(max(elves))
    # part 2
    elves.sort()
    print(elves[-1] + elves[-2] + elves[-3])

print(main())

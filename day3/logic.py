def find_item(rucksack):
    first = rucksack[:len(rucksack)//2]
    second = rucksack[len(rucksack)//2:]
    # The O(N^2) isn't ideal but it works
    for item in first:
        if item in second:
            return item

def item_priority(item):
    # Use ASCII values to easily convert to numbers
    value = ord(item)
    if value > 96:
        return value - 96
    return value - 38

def find_badge_item(rucksacks):
    s1 = set(rucksacks[0])
    s2 = set(rucksacks[1])
    s3 = set(rucksacks[2])

    set1 = s1.intersection(s2)
    final_set = set1.intersection(s3)
    return list(final_set)[0]

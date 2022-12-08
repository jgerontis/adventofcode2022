from logic import *

def test_find_item():
    assert(find_item("abcdEFGd") == "d")
    assert(find_item("vJrwpWtwJgWrhcsFMMfFFhFp") == "p")
    assert(find_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == "L")
    assert(find_item("PmmdzqPrVvPwwTWBwg") == "P")
    assert(find_item("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn") == "v")
    assert(find_item("ttgJtRGJQctTZtZT") == "t")
    assert(find_item("CrZsJsPPZsGzwwsLwLmpwMDw") == "s")

def test_item_priority():
    assert(item_priority("a") == 1)
    assert(item_priority("j") == 10)
    assert(item_priority("z") == 26)
    assert(item_priority("A") == 27)
    assert(item_priority("J") == 36)
    assert(item_priority("Z") == 52)

def test_find_badge_item():
    assert(find_badge_item(["vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg"]) == 'r')
    assert(find_badge_item(["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn","ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"]) == 'Z')


def tests():
    test_find_item()
    test_item_priority()
    test_find_badge_item()

tests()
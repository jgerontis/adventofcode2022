from logic import *

def test_outcome():
    assert(outcome("A","X") == 3)
    assert(outcome("A","Y") == 6)
    assert(outcome("A","Z") == 0)
    assert(outcome("B","X") == 0)
    assert(outcome("B","Y") == 3)
    assert(outcome("B","Z") == 6)
    assert(outcome("C","X") == 6)
    assert(outcome("C","Y") == 0)
    assert(outcome("C","Z") == 3)

def test_points_per_round():
    assert(points_per_round("A","X") == 4)
    assert(points_per_round("A","Y") == 8)
    assert(points_per_round("A","Z") == 3)
    assert(points_per_round("B","X") == 1)
    assert(points_per_round("B","Y") == 5)
    assert(points_per_round("B","Z") == 9)
    assert(points_per_round("C","X") == 7)
    assert(points_per_round("C","Y") == 2)
    assert(points_per_round("C","Z") == 6)

def test_calculate_move():
    assert(calculate_move("A", "X") == 3)
    assert(calculate_move("A", "Y") == 1)
    assert(calculate_move("A", "Z") == 2)
    assert(calculate_move("B", "X") == 1)
    assert(calculate_move("B", "Y") == 2)
    assert(calculate_move("B", "Z") == 3)
    assert(calculate_move("C", "X") == 2)
    assert(calculate_move("C", "Y") == 3)
    assert(calculate_move("C", "Z") == 1)

def test():
    test_outcome()
    test_points_per_round()
    test_calculate_move()

test()
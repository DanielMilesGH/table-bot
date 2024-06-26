import pytest 
from src.python.robots import BaseRobot

def handles_intint_coord_init():
    pos = (5,5)
    robot = BaseRobot(pos[0], pos[1])
    assert (robot.get_pos() == pos), "wrong position"

def handles_tuple_coord_init():
    pos = (5,5)
    robot = BaseRobot(pos[0], pos[1])
    assert (robot.get_pos() == pos), "wrong position"

def handles_bad_coord_init():
    invalid_positions = [
        (None, None),
        (5, None),
        (None, 5)
    ]

    for pos in invalid_positions:
        with pytest.raises(ValueError):
            BaseRobot(pos)
    
    for pos in invalid_positions:
        with pytest.raises(ValueError):
            BaseRobot(pos[0], pos[1])
        
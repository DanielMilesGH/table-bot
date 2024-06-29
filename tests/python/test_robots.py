import pytest 
from src.python.imports.robots import BaseRobot

def test_intint_coord_init():
    pos = (5,5)
    robot = BaseRobot(pos[0], pos[1])
    assert (robot.get_pos() == pos), "wrong position"

def test_tuple_coord_init():
    pos = (5,5)
    robot = BaseRobot(pos[0], pos[1])
    assert (robot.get_pos() == pos), "wrong position"

            
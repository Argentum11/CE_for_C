from run_command import *
import random
import math

#######################################################################
def create_abs_command(number):
    command = "|" + str(number) + "|"
    return command

def test_abs_positive():
    positive_integer = random.randint(0, 1000000)
    command = create_abs_command(positive_integer)
    expected_output = add_equal_sign(positive_integer)
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_abs_negative():
    positive_integer = random.randint(-1000000, -1)
    command = create_abs_command(positive_integer)
    expected_output = add_equal_sign(abs(positive_integer))
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)
from run_command import *
import random
import math

#######################################################################
def create_abs_command(number):
    command = f'{VAR}{ASSIGN}|{number}|{SEMICOLON}'
    return command

def test_abs_positive():
    positive_integer = random.randint(0, 1000000)
    command = create_abs_command(positive_integer)
    expected_output = f'{STORE} {VAR} {EQUAL} {positive_integer}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_abs_negative():
    negative_integer = random.randint(-1000000, -1)
    command = create_abs_command(negative_integer)
    expected_output = f'{STORE} {VAR} {EQUAL} {abs(negative_integer)}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)
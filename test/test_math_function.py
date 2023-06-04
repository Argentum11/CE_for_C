from run_command import *
import math

#######################################################################
def abs_command(number):
    command = f'cout<<|{number}|<<endl;'
    return command

def run_abs(number):
    command = abs_command(number)
    expected_output = f'{number}'
    if number<0:
        expected_output = f'{abs(number)}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_abs():
    # positive
    positive_integer = get_random_number(POSITIVE, INT)
    run_abs(positive_integer)

    # negative
    negative_integer = get_random_number(NEGATIVE, INT)
    run_abs(negative_integer)
#######################################################################
def degree_to_radian(degree):
    PI = 3.14159265359
    return f'{degree}*{PI}/180'

SIN = "sin"
COS = "cos"
TAN = "tan"

def trigonometric_command(function, radian):
    return f'cout<<{function}({radian})<<endl;'

sin_dict = {
    30: 0.5,
    60: 0.866025,
    90: 1
}

def run_sin(degree):
    radian = degree_to_radian(degree)
    command = trigonometric_command(SIN, radian)
    expected_output = sin_dict[degree]
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_sin():
    for degree in sin_dict.keys():
        run_sin(degree)
#######################################################################
cos_dict = {
    30: 0.866025,
    60: 0.5,
    180: -1
}

def run_cos(degree):
    radian = degree_to_radian(degree)
    command = trigonometric_command(COS, radian)
    expected_output = cos_dict[degree]
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_cos():
    for degree in cos_dict.keys():
        run_cos(degree)
#######################################################################
tan_dict = {
    30: 0.57735,
    45: 1,
    60: 1.73205,
    
}

def run_tan(degree):
    radian = degree_to_radian(degree)
    command = trigonometric_command(TAN, radian)
    expected_output = tan_dict[degree]
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_tan():
    for degree in tan_dict.keys():
        run_tan(degree)
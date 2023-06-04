from run_command import *

#######################################################################
def abs_command(number):
    command = f'cout<<|{number}|<<endl;'
    return command

def abs(number):
    command = abs_command(number)
    expected_output = f'{number}'
    if number<0:
        expected_output = f'{abs(number)}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_abs_positive():
    # positive
    positive_integer = get_random_number(POSITIVE, INT)
    abs(positive_integer)

    # negative
    negative_integer = get_random_number(POSITIVE, INT)
    abs(negative_integer)
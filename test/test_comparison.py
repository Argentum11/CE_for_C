from run_command import * 
# the following only test true conditions
expected_output = 1

def comparison_command(comparison:str):
    return f'cout<<({comparison})<<endl;'

def greater_than(num1, num2):
    command = comparison_command(f'{num1}>{num2}')
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_greater_than():
    num1 = get_random_number(POSITIVE, INT)
    num2 = number_for_command(num1+10)
    num1 = number_for_command(num1)
    greater_than(num2, num1)
#######################################################################
def greater_equal_than(num1, num2):
    command = comparison_command(f'{num1}>={num2}')
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_greater_equal_than():
    # greater than
    num1 = get_random_number(POSITIVE, INT)
    num2 = number_for_command(num1+10)
    num1 = number_for_command(num1)
    greater_equal_than(num2, num1)
    
    # equal than
    num1 = get_random_number(POSITIVE, INT)
    num1 = number_for_command(num1)
    greater_equal_than(num1, num1)
#######################################################################
def equal(num1):
    command = comparison_command(f'{num1}=={num1}')
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_equal():
    num1 = get_random_number(POSITIVE, INT)
    num1 = number_for_command(num1)
    equal(num1)
#######################################################################
def less_equal_than(num1, num2):
    command = comparison_command(f'{num1}<={num2}')
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)
    
def test_less_equal_than():
    # less than
    num1 = get_random_number(POSITIVE, INT)
    num2 = number_for_command(num1 - 10)
    num1 = number_for_command(num1)
    less_equal_than(num2, num1)

    # equal than
    num1 = get_random_number(POSITIVE, INT)
    less_equal_than(num1, num1)
#######################################################################    
def less_than(num1, num2):
    command = comparison_command(f'{num1}<{num2}')
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_less_than():
    num1 = get_random_number(POSITIVE, INT)
    num2 = number_for_command(num1 - 10)
    num1 = number_for_command(num1)
    less_than(num2, num1)
    
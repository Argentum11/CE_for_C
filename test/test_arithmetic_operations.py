from run_command import *
import random

POSITIVE = 1
NEGATIVE = -1
def get_random_integers(sign):
    integer = random.randint(0, 100) * sign
    return integer

combination={(POSITIVE, POSITIVE), (POSITIVE, NEGATIVE), (NEGATIVE, POSITIVE), (NEGATIVE, NEGATIVE)}

#######################################################################
def create_add_command(augend, addend):
    augend = adjust_number_for_command(augend)
    addend = adjust_number_for_command(addend)
    command = str(augend)+ "+" + str(addend)
    return command

def addition(augend, addend):
    total = augend + addend
    expected_output = add_equal_sign(total)
    command = create_add_command(augend, addend)
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_addition():
    for x in combination:
        augend_sign = x[0]
        addend_sign = x[1]
        augend = get_random_integers(augend_sign)
        addend = get_random_integers(addend_sign)
        addition(augend, addend)

#######################################################################
def create_subtract_command(minuend, subtrahend):
    minuend = adjust_number_for_command(minuend)
    subtrahend = adjust_number_for_command(subtrahend)
    command = str(minuend)+ "-" + str(subtrahend)
    return command

def subtraction(minuend, subtrahend):
    difference = minuend - subtrahend
    expected_output = add_equal_sign(difference)
    command = create_subtract_command(minuend, subtrahend)
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_subtraction():
    for x in combination:
        augend_sign = x[0]
        subtrahend_sign = x[1]
        minuend = get_random_integers(augend_sign)
        subtrahend = get_random_integers(subtrahend_sign)
        subtraction(minuend, subtrahend)

#######################################################################
def create_multiply_command(multiplicand, multiplier):
    multiplicand = adjust_number_for_command(multiplicand)
    multiplier = adjust_number_for_command(multiplier)
    command = str(multiplicand)+ "*" + str(multiplier)
    return command

def multiplication(multiplicand, multiplier):
    product = multiplicand * multiplier
    expected_output = add_equal_sign(product)
    command = create_multiply_command(multiplicand, multiplier)
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_multiplication():
    for x in combination:
        multiplicand_sign = x[0]
        multiplier_sign = x[1]
        minuend = get_random_integers(multiplicand_sign)
        multiplier = get_random_integers(multiplier_sign)
        multiplication(minuend, multiplier)

#######################################################################
def create_divide_command(dividend, divisor):
    dividend = adjust_number_for_command(dividend)
    divisor = adjust_number_for_command(divisor)
    command = str(dividend)+ "/" + str(divisor)
    return command

def division(dividend, divisor):
    quotient = int(dividend / divisor)
    expected_output = add_equal_sign(quotient)
    command = create_divide_command(dividend, divisor)
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_division():
    for x in combination:
        dividend_sign = x[0]
        divisor_sign = x[1]
        dividend = get_random_integers(dividend_sign)
        divisor = get_random_integers(divisor_sign)
        division(dividend, divisor)

#######################################################################
def create_parenthesis_command(num_1, num_2, num_3):
    # num_1*(num_2+num_3)
    command = str(num_1) + "*(" + str(num_2) + "+" + str(num_3)+ ")"
    return command

def parenthesis(num_1, num_2, num_3):
    command = create_parenthesis_command(num_1, num_2, num_3)
    expected_output = add_equal_sign( num_1 * (num_2+num_3) )
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_parenthesis():
    num_1 = get_random_integers(POSITIVE)
    num_2 = get_random_integers(POSITIVE)
    num_3 = get_random_integers(POSITIVE)
    parenthesis(num_1, num_2, num_3)
    
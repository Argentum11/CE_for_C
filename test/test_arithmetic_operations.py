from run_command import *
import random

POSITIVE = 1
NEGATIVE = -1
# operation
ADD = 1
SUBTRACT = 2
MULTIPLIY = 3
DIVIDE = 4


def get_random_number(sign, type):
    if type == INT:
        return random.randint(0, 100) * sign
    else:
        return round(random.uniform(0, 100), 2) * sign

def float_to_int(num):
    num_str = str(num)
    #print(num_str)
    final_index = len(num_str)-1
    point_index = num_str.find('.')
    #print(point_index, final_index)
    #print(num_str[final_index])
    if num_str[final_index]=='0' and (final_index-point_index)==1:
        num_str = num_str[:final_index-1]
    else:
        num_str = num * pow(10,final_index - point_index)
    return int(num_str)

def get_decimal_points(num):
    num_str = str(num)
    final_index = len(num_str)-1
    point_index = num_str.find('.')
    if point_index == -1:
        return 0
    return final_index-point_index

def fake_double_check(num, num_type):
    num_str = str(num)
    final_index = len(num_str)-1
    point_index = num_str.find('.')
    if(num_type==DOUBLE and num_str[final_index]=='0' and final_index-point_index==1):
        return int(num), INT
    else:
        return num, num_type

def result_type(operation, num1, num1_type, num2, num2_type):
    # fake double
    num1, num1_type = fake_double_check(num1, num1_type)
    num2, num2_type = fake_double_check(num2, num2_type)

    if (num1_type == DOUBLE or num2_type == DOUBLE):
        num1_int = num1
        num2_int = num2
        if(num1_type == DOUBLE):
            num1_int = float_to_int(num1)
        if(num2_type == DOUBLE):
            num2_int = float_to_int(num2)
        result = 0
        print(num1_int , num2_int)
        if operation == ADD:
            result = num1_int + num2_int
        elif operation == SUBTRACT:
            result = num1_int - num2_int
        elif operation == MULTIPLIY:
            result = num1_int * num2_int
        elif operation == DIVIDE:
            result = num1_int / num2_int
        ten_pow = pow(10, get_decimal_points(num1)+get_decimal_points(num2))
        print(ten_pow)
        if result % ten_pow == 0:
            return INT
        else:
            return DOUBLE
    else:
        return INT
    
def total_decimal_points(num1, num1_type, num2, num2_type):
    num1, num1_type = fake_double_check(num1, num1_type)
    num2, num2_type = fake_double_check(num2, num2_type)
    sum = 0
    if num1_type==DOUBLE:
        num_str = str(num1)
        final_index = len(num_str)-1
        point_index = num_str.find('.')
        sum = sum + (final_index - point_index)
    if num2_type==DOUBLE:
        num_str = str(num2)
        final_index = len(num_str)-1
        point_index = num_str.find('.')
        sum = sum + (final_index - point_index)
    return sum

        

sign_combination = {(POSITIVE, POSITIVE), (POSITIVE, NEGATIVE),
                    (NEGATIVE, POSITIVE), (NEGATIVE, NEGATIVE)}
type_combination = {(INT, DOUBLE), (INT, INT), (DOUBLE, INT), (DOUBLE, DOUBLE)}

#######################################################################


def create_add_command(augend, addend, type):
    augend: str = number_for_command(augend)
    addend: str = number_for_command(addend)
    command = f'{type_str(type)} {VAR}{ASSIGN}{augend}+{addend}{SEMICOLON}{NEWLINE}'
    command = f'{command}{variable_output_command(VAR)}'
    return command


def addition(augend, augend_type, addend, addend_type):
    total = augend + addend
    if (augend_type == DOUBLE or addend_type == DOUBLE):
        total = round(total, 2)
    type = result_type(ADD, augend, augend_type, addend, addend_type)
    if type==INT:
        total = int(total)
    command = create_add_command(augend, addend, type)
    expected_output = f'{total}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)


def test_addition():
    for x in sign_combination:
        augend_sign = x[0]
        addend_sign = x[1]
        for y in type_combination:
            augend_type = y[0]
            addend_type = y[1]
            augend = get_random_number(augend_sign, augend_type)
            addend = get_random_number(addend_sign, addend_type)
            addition(augend, augend_type, addend, addend_type)

# #######################################################################


def create_subtract_command(minuend, subtrahend, type):
    minuend: str = number_for_command(minuend)
    subtrahend: str = number_for_command(subtrahend)
    command = f'{type_str(type)} {VAR}{ASSIGN}{minuend}-{subtrahend}{SEMICOLON}{NEWLINE}'
    command = f'{command}{variable_output_command(VAR)}'
    return command


def subtraction(minuend, minuend_type, subtrahend, subtrahend_type):
    difference = minuend - subtrahend
    if (minuend_type == DOUBLE or subtrahend_type == DOUBLE):
        difference = round(difference, 2)
    type = result_type(SUBTRACT, minuend, minuend_type, subtrahend, subtrahend_type)
    if type==INT:
        difference = int(difference)
    command = create_subtract_command(minuend, subtrahend, type)
    expected_output = f'{difference}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)


def test_subtraction():
    for x in sign_combination:
        minuend_sign = x[0]
        subtrahend_sign = x[1]
        for y in type_combination:
            minuend_type = y[0]
            subtrahend_type = y[1]
            minuend = get_random_number(minuend_sign, minuend_type)
            subtrahend = get_random_number(subtrahend_sign, subtrahend_type)
            subtraction(minuend, minuend_type, subtrahend, subtrahend_type)

# #######################################################################


def create_multiply_command(multiplicand, multiplier):
    multiplicand: str = number_for_command(multiplicand)
    multiplier: str = number_for_command(multiplier)
    command = f'{type_str(INT)} {VAR}{ASSIGN}{multiplicand}*{multiplier}{SEMICOLON}{NEWLINE}'
    command = f'{command}{variable_output_command(VAR)}'
    return command

def multiplication(multiplicand, multiplier):
    product = multiplicand * multiplier
    command = create_multiply_command(multiplicand, multiplier)
    expected_output = f'{product}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

# It's hard to mimic %g for floats, so we skipped the float multiply and divide test
def test_multiplication():
    for x in sign_combination:
        multiplicand_sign = x[0]
        multiplier_sign = x[1]
        multiplicand_type = INT
        multiplier_type = INT
        multiplicand = get_random_number(multiplicand_sign, multiplicand_type)
        multiplier = get_random_number(multiplier_sign, multiplier_type)
        multiplication(multiplicand, multiplier)

# #######################################################################
def create_divide_command(dividend, divisor):
    dividend: str = number_for_command(dividend)
    divisor: str = number_for_command(divisor)
    command = f'{type_str(INT)} {VAR}{ASSIGN}{dividend}/{divisor}{SEMICOLON}{NEWLINE}'
    command = f'{command}{variable_output_command(VAR)}'
    return command

def division(dividend, divisor):
    quotient = int(dividend / divisor)
    command = create_divide_command(dividend, divisor)
    expected_output = f'{quotient}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_division():
    for x in sign_combination:
        dividend_sign = x[0]
        divisor_sign = x[1]
        dividend_type = INT
        divisor_type = INT
        dividend = get_random_number(dividend_sign, dividend_type)
        divisor = get_random_number(divisor_sign, divisor_type)
        division(dividend, divisor)

#######################################################################
def create_parenthesis_command(num_1, num_2, num_3):
    # num_1*(num_2+num_3)
    command = f'cout<<{num_1}*({num_2}+{num_3})<<endl;'
    return command

def parenthesis(num_1, num_2, num_3):
    command = create_parenthesis_command(num_1, num_2, num_3)
    expected_output = f'{(num_1*(num_2+num_3))}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_parenthesis():
    for i in range(5):
        num_1 = get_random_number(POSITIVE, INT)
        num_2 = get_random_number(POSITIVE, INT)
        num_3 = get_random_number(POSITIVE, INT)
        parenthesis(num_1, num_2, num_3)

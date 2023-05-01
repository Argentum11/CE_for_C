from run_command import *
import string
import random
LETTER = 0
NUMBER = 1

INT = 2
#DOUBLE = 3
#CHAR = 4 for string, 5 for char
variable_type_list = [INT]

NEW_VAR = 6
VAR_REASSIGNMENT = 7
OUTPUT_VAR = 8
VAR_MATH = 9
action_list = [NEW_VAR, VAR_REASSIGNMENT, OUTPUT_VAR]

VAR_MAX_LENGTH = 9

class Variable:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value
    def reassign_value(self, value):
        self.value = value

variable_list = []

def generate_letter():
    random_letter = random.choice(string.ascii_letters)
    return random_letter

def generate_letter_or_number():
    choice = random.randint(0, 2)
    if choice == LETTER:
        return generate_letter()
    else:
        number = random.randint(0, 9)
        return str(number)

def generate_variable_name():
    variable_name = ""
    variable_length = random.randint(1, VAR_MAX_LENGTH)
    for i in range(0, variable_length):
        if i==0:
            variable_name = variable_name + generate_letter()
        else:
            variable_name = variable_name + generate_letter_or_number()
    return variable_name

def generate_variable_value(type):
    value = 14641
    if type == INT:
        value = random.randint(-1000, 1000)
    return value

def generate_variable():
    name = generate_variable_name()
    type = random.choice(variable_type_list)
    value = generate_variable_value(type)
    variable = Variable(name, type, value)
    return variable

def variable_declaration(variable:Variable):
    command = f'{variable.name}{ASSIGN}{adjust_number_for_command(variable.value)}{SEMICOLON}'
    expected_output = f'store {variable.name} = {variable.value}'
    case = Case(command, expected_output)
    return case

def case_end(command, expected_output):
    newLine= truth_or_false()
    end = ""
    if newLine:
        end = f'<<{ENDL}'
    end = f'{end}{SEMICOLON}'
    command = f'{command}{end}'
    case = Case(command, expected_output)
    if newLine==False:
        case.expected_output = delete_newline(case.expected_output)
    return case

def output_variable(variable:Variable):
    command = f'{COUT}<<{variable.name}'
    expected_output = variable.value
    return case_end(command, expected_output)

def output_multiple_variables(selected_variables:list):
    variable_name_concatenation = ""
    variable_value_concatenation = ""
    variable:Variable
    if len(selected_variables)>0:
        for variable in selected_variables:
            variable_name_concatenation = f'{variable_name_concatenation}<<{variable.name}'
            variable_value_concatenation = f'{variable_value_concatenation}{variable.value}'
    command = f'{COUT}{variable_name_concatenation}'
    expected_output = variable_value_concatenation
    return case_end(command, expected_output)

def variable_reassignment(variable:Variable):
    new_value = generate_variable_value(variable.type)
    variable.reassign_value(new_value)
    return variable_declaration(variable)
    
def test_variable_assignment():
    case_list = []
    for i in range(0, 10):
        action = -1
        if len(variable_list)==0 :
            action = NEW_VAR
        else:
            action = random.choice(action_list)

        print(action)
        if action == NEW_VAR:
            new_variable = generate_variable()
            variable_list.append(new_variable)
            case_list.append(variable_declaration(new_variable))
            case_list.append(output_variable(new_variable))
        elif action == VAR_REASSIGNMENT:
            existing_variable:Variable = random.choice(variable_list)
            case_list.append(variable_reassignment(existing_variable))
            case_list.append(output_variable(existing_variable))
        elif action == OUTPUT_VAR:
            output_var_list = []
            for var in variable_list:
                if truth_or_false():
                    output_var_list.append(var)
            if len(output_var_list)==0:
                output_var_list.append(random.choice(variable_list))
            case_list.append(output_multiple_variables(output_var_list))
    command = ""
    expected_output = ""
    current_case:Case
    for current_case in case_list:
        command = f'{command}{current_case.command}'
        expected_output = f'{expected_output}{current_case.expected_output}'
    total_case = Case(command, expected_output)
    delete_newline_for_case(total_case)
    assert total_case.expected_output == run_command(total_case)

VARIABLE = 10
operand_list = [NUMBER, VARIABLE]
operand_combination = {(NUMBER, VARIABLE), (VARIABLE, NUMBER), (VARIABLE, VARIABLE)}

def generate_five_variables():
    for i in range(5):
        new_variable:Variable = generate_variable()
        variable_list.append(new_variable)

def get_operand(type:int):
    if type==VARIABLE:
        return random.choice(variable_list)
    else:
        return random.randint(-1000, 1000)
    
def operand_decoder(operand):
    name = ""
    value = 0
    if isinstance(operand, Variable):
        name = operand.name
        value = operand.value
    else:
        name = adjust_number_for_command(operand)
        value = operand
    return name, value

#######################################################################
def prepare_variable():
    variable_list.clear()
    generate_five_variables()
    command = ""
    expected_output = ""
    var:Variable
    for var in variable_list:
        command = f'{command}{var.name}{ASSIGN}{adjust_number_for_command(var.value)}{SEMICOLON}{NEWLINE}'
        expected_output = f'{expected_output}store {var.name} = {var.value}{NEWLINE}'
    prepared_case = Case(command, expected_output)
    delete_newline_for_case(prepared_case)
    return prepared_case

#######################################################################
def variable_add(previous_case:Case, operand1, operand2):
    name1, value1  = operand_decoder(operand1)
    name2, value2  = operand_decoder(operand2)
    sum = value1 + value2
    command = f'{previous_case.command}{VAR}{ASSIGN}{name1}+{name2}{SEMICOLON}'
    expected_output = f'{previous_case.expected_output}store {VAR} = {sum}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_variable_add():
    prepared_case:Case = prepare_variable() 
    for operand_pair in operand_combination:
        operand1 = get_operand(operand_pair[0])
        operand2 = get_operand(operand_pair[1])
        variable_add(prepared_case, operand1, operand2)

#######################################################################
def variable_subtraction(previous_case:Case, operand1, operand2):
    name1, value1  = operand_decoder(operand1)
    name2, value2  = operand_decoder(operand2)
    difference = value1 - value2
    command = f'{previous_case.command}{VAR}{ASSIGN}{name1}-{name2}{SEMICOLON}'
    expected_output = f'{previous_case.expected_output}store {VAR} = {difference}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_variable_subtraction():
    prepared_case:Case = prepare_variable() 
    for operand_pair in operand_combination:
        operand1 = get_operand(operand_pair[0])
        operand2 = get_operand(operand_pair[1])
        variable_subtraction(prepared_case, operand1, operand2)

#######################################################################
def variable_multiplication(previous_case:Case, operand1, operand2):
    name1, value1  = operand_decoder(operand1)
    name2, value2  = operand_decoder(operand2)
    product = value1 * value2
    command = f'{previous_case.command}{VAR}{ASSIGN}{name1}*{name2}{SEMICOLON}'
    expected_output = f'{previous_case.expected_output}store {VAR} = {product}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_variable_multiplication():
    prepared_case:Case = prepare_variable() 
    for operand_pair in operand_combination:
        operand1 = get_operand(operand_pair[0])
        operand2 = get_operand(operand_pair[1])
        variable_multiplication(prepared_case, operand1, operand2)

#######################################################################
def variable_division(previous_case:Case, operand1, operand2):
    name1, value1  = operand_decoder(operand1)
    name2, value2  = operand_decoder(operand2)
    quotient = int(value1 / value2)
    command = f'{previous_case.command}{VAR}{ASSIGN}{name1}/{name2}{SEMICOLON}'
    expected_output = f'{previous_case.expected_output}store {VAR} = {quotient}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_variable_division():
    prepared_case:Case = prepare_variable() 
    for operand_pair in operand_combination:
        operand1 = get_operand(operand_pair[0])
        operand2 = get_operand(operand_pair[1])
        variable_division(prepared_case, operand1, operand2)

#######################################################################
def variable_parenthesis(previous_case:Case, operand1, operand2, operand3):
    name1, value1  = operand_decoder(operand1)
    name2, value2  = operand_decoder(operand2)
    name3, value3  = operand_decoder(operand3)
    result = value1 * (value2 + value3)
    command = f'{previous_case.command}{VAR}{ASSIGN}{name1}*({name2}+{name3}){SEMICOLON}'
    expected_output = f'{previous_case.expected_output}store {VAR} = {result}'
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_variable_division():
    prepared_case:Case = prepare_variable() 
    for operand_pair in operand_combination:
        operand1 = get_operand(operand_pair[0])
        operand2 = get_operand(operand_pair[1])
        operand3 = get_operand(operand_pair[0])
        variable_parenthesis(prepared_case, operand1, operand2, operand3)
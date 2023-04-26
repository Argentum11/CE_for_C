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
PRINT_VAR = 8
action_list = [NEW_VAR, VAR_REASSIGNMENT, PRINT_VAR]

VAR_MAX_LENGTH = 9
ASSIGN = "="
EXPRESSION_END = ";"

class Variable:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value
    def reassign_value(self, value):
        self.value = value

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

def variable_declaration(variable_name, variable_value):
    command = variable_name + ASSIGN + str(adjust_number_for_command(variable_value)) + EXPRESSION_END
    expected_output = "store " + variable_name + " = "+ str(variable_value)
    case = Case(command, expected_output)
    return case

def print_variable(variable_name, variable_value):
    command = "print " + str(variable_name) + ";"
    expected_output = variable_value
    case = Case(command, expected_output)
    return case

def variable_reassignment(variable_name, variable_value):
    return variable_declaration(variable_name, variable_value)
    
def test_variable():
    variable_list = []
    case_list = []
    for i in range(0, 10):
        action = -1
        if len(variable_list)==0 :
            action = NEW_VAR
        else:
            action = random.choice(action_list)

        if action == NEW_VAR:
            name = generate_variable_name()
            type = random.choice(variable_type_list)
            value = generate_variable_value(type)
            new_variable = Variable(name, type, value)
            variable_list.append(new_variable)
            case_list.append(variable_declaration(new_variable.name, new_variable.value))
            case_list.append(print_variable(new_variable.name, new_variable.value))
        elif action == VAR_REASSIGNMENT:
            existing_variable = random.choice(variable_list)
            new_value = generate_variable_value(existing_variable.type)
            existing_variable.reassign_value(new_value)
            case_list.append(variable_reassignment(existing_variable.name, existing_variable.value))
            case_list.append(print_variable(existing_variable.name, existing_variable.value))
        elif action == PRINT_VAR:
            existing_variable = random.choice(variable_list)
            case_list.append(print_variable(existing_variable.name, existing_variable.value))

    command = ""
    expected_output = ""
    for current_case in case_list:
        command = command + current_case.command
        expected_output = expected_output + current_case.expected_output
    total_case = Case(command, expected_output)
    fix_case_for_multiple_command(total_case)
    assert total_case.expected_output == run_command(total_case)
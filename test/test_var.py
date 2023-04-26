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
OUTPUT_MULTIPLE_VAR = 9
action_list = [NEW_VAR, VAR_REASSIGNMENT, OUTPUT_VAR, OUTPUT_MULTIPLE_VAR]

VAR_MAX_LENGTH = 9

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
    command = f'{variable_name}{ASSIGN}{adjust_number_for_command(variable_value)}{SEMICOLON}'
    expected_output = f'store {variable_name} = {variable_value}'
    case = Case(command, expected_output)
    return case

def case_end(command, expected_output):
    newLine= truth_or_false()
    end = ""
    if newLine:
        end = f'<<{ENDL}'
    end = f'{end}{SEMICOLON}'
    command = f'{command}{end}'
    case = Case(command, expected_output, newLine)
    return case

def output_variable(variable_name, variable_value):
    command = f'{COUT}<<{variable_name}'
    expected_output = variable_value
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

        print(action)
        if action == NEW_VAR:
            name = generate_variable_name()
            type = random.choice(variable_type_list)
            value = generate_variable_value(type)
            new_variable = Variable(name, type, value)
            variable_list.append(new_variable)
            case_list.append(variable_declaration(new_variable.name, new_variable.value))
            case_list.append(output_variable(new_variable.name, new_variable.value))
        elif action == VAR_REASSIGNMENT:
            existing_variable = random.choice(variable_list)
            new_value = generate_variable_value(existing_variable.type)
            existing_variable.reassign_value(new_value)
            case_list.append(variable_reassignment(existing_variable.name, existing_variable.value))
            case_list.append(output_variable(existing_variable.name, existing_variable.value))
        elif action == OUTPUT_VAR:
            existing_variable:Variable = random.choice(variable_list)
            case_list.append(output_variable(existing_variable.name, existing_variable.value))
        elif action == OUTPUT_MULTIPLE_VAR:
            output_var_list = []
            for var in variable_list:
                if truth_or_false():
                    output_var_list.append(var)
            if len(output_var_list)==0:
                output_var_list.append(variable_list[0])
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
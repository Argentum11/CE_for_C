import random

class Case:
  def __init__(self, command, expected_output):
    self.command = f'{command}\n'
    self.expected_output = f'{expected_output}\n'

def run_command(case:Case):
  import subprocess
  command =case.command
  with open("input.txt",'w') as my_file:
      my_file.write(command)
  command = '..\\a.exe'
  in_sign = "<"
  in_file = "input.txt"
  out_sign = ">"
  out_file = "result.txt"
  subprocess.run([command, in_sign, in_file, out_sign, out_file], shell=True)

  with open("result.txt") as my_file:
      output = my_file.read()
  return output

def number_for_command(number):
    if(number < 0):
        result = f'({number})'
    else:
        result = str(number)
    return result

#delete additional \n at the end
def delete_newline(text):
    final_index = len(text)-1
    return text[:final_index]

def delete_newline_for_case(case:Case):
   case.command = delete_newline(case.command)
   case.expected_output = delete_newline(case.expected_output)

def truth_or_false():
   return random.choice([True, False])

def variable_output_command(variable_name:str):
   return f'cout<<{variable_name}<<endl;'

# Global constants
VAR = "a1"
ASSIGN = "="
EQUAL = "="
SEMICOLON = ";"
STORE = "store"
COUT = "cout"
ENDL = "endl"
NEWLINE = "\n"

INT = 2
DOUBLE = 3
STRING = 4
POSITIVE = 1
NEGATIVE = -1
variable_type_list = [INT, DOUBLE]

def type_str(type:int):
    if type == INT:
      return "int"
    elif type == DOUBLE:
        return "double"
    else:
       return "string"
    
def get_random_number(sign, type):
    if type == INT:
        random_number = 0
        while random_number==0:
            random_number = random.randint(0, 100) * sign
        return random_number
    else:
        return round(random.uniform(0, 100), 2) * sign
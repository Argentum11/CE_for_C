class Case:
  def __init__(self, command, expected_output):
    self.command = command + "\n"
    self.expected_output = str(expected_output) + "\n"

def run_command(case):
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

def add_equal_sign(number):
    result = "=" + str(number)
    return result

def adjust_number_for_command(number):
    if(number < 0):
        result = "(" + str(number) + ")"
    else:
        result = number
    return result

#delete additional \n at the end
def fix_case_for_multiple_command(case:Case):
   command_final_index = len(case.command)-1
   case.command = case.command[:command_final_index]
   expected_output_final_index = len(case.expected_output)-1
   case.expected_output = case.expected_output[:expected_output_final_index]

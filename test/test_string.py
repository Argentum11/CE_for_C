from run_command import *

def string_command(symbol):
    return f'cout<<"{symbol}"<<endl;'

def test_tab():
    command = string_command(f'\\t')
    expected_output = TAB
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_newline():
    command = string_command("\\n")
    expected_output = NEWLINE
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

SINGLE_QUOTE = "'"
def test_single_quote():
    command = string_command(SINGLE_QUOTE)
    expected_output = SINGLE_QUOTE
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

DOUBLE_QUOTE = "\""
def test_double_quote():
    command = string_command(DOUBLE_QUOTE)
    expected_output = DOUBLE_QUOTE
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

BACK_SLASH = "\\\\"
def test_back_slash():
    command = string_command(BACK_SLASH)
    expected_output = "\\"
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_end_of_string():
    command = string_command("ab\\0c")
    expected_output = "ab"
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_normal_string():
    command = string_command("abc")
    expected_output = "abc"
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

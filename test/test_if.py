from run_command import *
def run_if(condition):
    command = f'if({condition})'+"{cout<<123<<endl;}"
    expected_output = 123
    case = Case(command, expected_output)
    assert case.expected_output == run_command(case)

def test_if():
    run_if("10>5")
    run_if("45<2304")
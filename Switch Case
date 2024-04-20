#a simple prorgam in Python 3 implementing switch case:

def case1():
    return "This is case 1"

def case2():
    return "This is case 2"

def case3():
    return "This is case 3"

def default_case():
    return "Default case"

switch = {
    1: case1,
    2: case2,
    3: case3,
}

def switch_case(argument):
    return switch.get(argument, default_case)()

print(switch_case(1))
print(switch_case(2))
print(switch_case(3))
print(switch_case(4))

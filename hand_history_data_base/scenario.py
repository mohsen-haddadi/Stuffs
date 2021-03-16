def search_a_module(scenario_number, module):
    # returns a string. it can returns None,
    # but base on the code it's not logical to return None.
    with open('decision_making/%s.py' %module) as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if 'scenario(%s)' %scenario_number in line \
        and line[:line.index('scenario(')].isspace():

            for back in range(i):
                if 'def ' in lines[i-back] and lines[i-back].index('def') == 0:
                    # https://stackoverflow.com/questions/3368969/find-string-between-two-substrings
                    function_name = lines[i-back][lines[i-back].find('def ')+len('def '):lines[i-back].rfind(':')]
                    return function_name

def return_play_function_name(scenario_number):
    if search_a_module(scenario_number, 'play') != None:
        return search_a_module(scenario_number, 'play')
    else:
        return search_a_module(scenario_number, 'play_raise')


# print(return_play_function_name(165)) # test

"""
This module will open play module and write scenario() functions 
before return statments.
"""
scenario_count = 1

def modify_play_module_code(module):
    global scenario_count
    modified_code = []
    
    with open('%s.py'% module, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if 'return ' in line:
            if '#' in line and line.index('#') < line.index('return '):
                modified_code.append(line)
            else:
                space_idents = line.index('return ')
                if 'scenario(' in lines[i-1] \
                and not( '#' in lines[i-1] and lines[i-1].index('#') < lines[i-1].index('scenario(') ):
                    modified_code.pop(-1)
                modified_code.append(space_idents * ' ' + 'scenario(%s)\n' 
                                     %scenario_count)
                scenario_count += 1
                modified_code.append(line)
        else:
            modified_code.append(line)

    with open('%s.py'% module, 'w') as file:
        file.writelines(modified_code)

if __name__ == '__main__':
    modify_play_module_code('play_version_1')
    #modify_play_module_code('play_raise_version_1')

print(scenario_count)
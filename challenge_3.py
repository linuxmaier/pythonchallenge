import string
import re

def find_pattern(file):
    '''returns a string that consists of the middle letters of matched xXXXxXXXx patterns in file''
    f = open(file, 'r')
    string_list = []
    return_string = ''
    pattern = re.compile('(?<![A-Z0-9])[A-Z]{3}([a-z])(?<![A-Z])[A-Z]{3}(?![A-Z0-9])')
    
    for line in f:
        string_list.extend(pattern.findall(line))
    for char in string_list:
        return_string += char
    return return_string

import string

def find_word(file):
    '''returns a dictionary of characters that occur with less than average frequency in file.'''
    f = open(file, 'r')
    more_lines = True
    char_frequencies = dict()

    while more_lines:
        current_line = f.readline()

        if current_line != '':
            for char in current_line:
                try:
                    char_frequencies[char] += 1
                except KeyError:
                    char_frequencies[char] = 1
        else:
            more_lines = False

    average_value = 0
    for item in char_frequencies:
        average_value += char_frequencies.get(item)
    average_value /= len(char_frequencies)

    for k, v in list(char_frequencies.items()):
        if char_frequencies.get(k) > average_value:
            del char_frequencies[k]
    
    return char_frequencies




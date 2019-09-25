# -*- coding: utf-8 -*-


def char_counts(textfilename):
    infile = open(textfilename, encoding='utf-8')
    file_string = infile.read().strip()  # reads file and removes whitespace
    character_count = {i: 0 for i in list(range(256))}  # make dictionary of utf-codes with count 0
    for c in file_string:
        character_count[ord(c)] += 1
    result = list(character_count.values())
    infile.close()
    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )

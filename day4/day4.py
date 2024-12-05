import argparse
import re

def parse_args():
    """Returns args, wrapper for ArgumentParser config and call"""

    parser = argparse.ArgumentParser(
            prog='day4.py',
            description='Advent of Code day 4')

    parser.add_argument('filename',
                        help='input filename')
    parser.add_argument('-2', '--part2', action='store_true', default=False,
                        help='perform part 2 of the puzzle!')

    args = parser.parse_args()

    return args


def dbgprintfield(field):
    """Prints the field"""

    for line in field:
        for char in line:
            print(' %c' % char, end = '')
        print()


def read_input_into_field(filename):
    """Returns a list of lines of the text in the file"""

    word_field = []
    add_row = word_field.append

    for line in open(filename, 'r'):
        add_row(line)

    return word_field


def read_word_at_position_in_direction(x, y, direction, word, field):
    """Returns 1 if a word exists at a given position and direction"""

    x_dir = direction[0]
    y_dir = direction[1]
    x_range = (x,) * len(word) if x_dir == 0 else range(x, x + len(word) * x_dir, x_dir)
    y_range = (y,) * len(word) if y_dir == 0 else range(y, y + len(word) * y_dir, y_dir)

    read = ''.join([field[y][x] for x, y in zip(x_range, y_range)])

    if read == word:
        print('found %s at %d, %d going (%d, %d)' % (word, x, y, x_dir, y_dir))
    return read == word


def check_for_word_at(x, y, word, field):
    """Checks if a word starts at the given position in all 8 directions"""

    length = len(field[0])
    height = len(field)
    clearance = len(word) - 1
    count = 0

    #     → +x
    #   ↓ 
    #   +y

    #directions
    directions = {
            "UP_LEFT"    : (-1, -1),
            "UP"         : ( 0, -1),
            "UP_RIGHT"   : ( 1, -1),
            "LEFT"       : (-1,  0),
            "RIGHT"      : ( 1,  0),
            "DOWN_LEFT"  : (-1,  1),
            "DOWN"       : ( 0,  1),
            "DOWN_RIGHT" : ( 1,  1)
        }

    for k, v in directions.items():
        word_end = (x + v[0] * clearance, y + v[1] * clearance)

        #if our word can fit given it's positionand direction
        if (0 <= word_end[0] and word_end[0] < length) and \
           (0 <= word_end[1] and word_end[1] < height):

               #try to read it!
               count += 1 if read_word_at_position_in_direction(x, y, v, word, field) else 0

    return count


def word_search_count(word, field):
    """Returns the number of times the target word appears in a word search"""

    length = len(field[0])
    height = len(field)
    count = 0

    #8 directions available, dictated by position
    '''
    ↖ ↑ ↗ can't do when we aren't down enough
    ←   →
    ↙ ↓ ↘ can't do when we are too down
    ^
    can't do when we aren't right enough
        ^ can't do when we are too right
    '''

    for y in range(height):
        for x in range(length):
            count += check_for_word_at(x, y, word, field)

    return count


def check_for_cross_word_at(x, y, word, field):
    """Checks a specific position for the presence of a cross word"""

    start = word[0]
    center = word[1]
    end = word[2]

    if field[y][x] != center:
        return False

    #only have to check 2 adjacent "corners" of the cross
    '''
    M . S
    . A .
    M . S
    '''

    #upper left corner word
    x_range = range(x - 1, x + 2)
    y_range = range(y - 1, y + 2)
    upper_left = ''.join([field[y][x] for x, y in zip(x_range, y_range)])

    if upper_left != word and upper_left[::-1] != word:
        return False

    #upper right corner word
    x_range = range(x + 1, x - 2, -1)
    y_range = range(y - 1, y + 2)
    upper_right = ''.join([field[y][x] for x, y in zip(x_range, y_range)])

    if upper_right != word and upper_right[::-1] != word:
        return False

    print('Found a cross of %s at %d, %d' % (word, x, y))
    return True
    

def cross_word_search_count(word, field):
    """Returns the number of times the target cross word appears in a cross word search"""

    if(len(word) != 3):
        raise Exception('This only works for words of length 3, like \'MAS\' :)')

    length = len(field[0]) - 1
    height = len(field) - 1
    count = 0

    #We can check locations for the center of the cross
    #So we can trim off the first and last col and row
    for y in range(1, height):
        for x in range(1, length):
            count += 1 if check_for_cross_word_at(x, y, word, field) else 0

    return count


def cli_main(args):
    """main entry"""

    TARGET_WORD = "XMAS"
    TARGET_CROSS = "MAS"

    word_field = read_input_into_field(args.filename)

    if args.part2:
        word_count = cross_word_search_count(TARGET_CROSS, word_field)
    else:
        word_count = word_search_count(TARGET_WORD, word_field)

    print('Found %s %d times!' % (TARGET_WORD, word_count))


if __name__ == '__main__':

    args = parse_args()
    cli_main(args)



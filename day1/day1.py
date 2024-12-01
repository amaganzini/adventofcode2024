import argparse

def parse_args():
    """Returns args, wrapper for ArgumentParser config and call"""

    parser = argparse.ArgumentParser(
            prog='day1.py',
            description='Advent of Code day 1')

    parser.add_argument('filename', default='input.txt', nargs='?',
                        help='input filename')
    parser.add_argument('-2', '--part2', action='store_true', default=False,
                        help='perform part 2 of the puzzle!')

    args = parser.parse_args()

    return args


def read_input_cols(filename):
    """Returns the left and right columns from the input filename as lists"""

    left_col = []
    right_col = []
    left_append = left_col.append
    right_append = right_col.append

    for line in open(filename, 'r'):

        left_val, right_val = line.split()

        left_append(int(left_val))
        right_append(int(right_val))

    return left_col, right_col


def calc_distance(left_col, right_col):
    """Returns the distance score between two lists"""

    left_sort = sorted(left_col)
    right_sort = sorted(right_col)

    distances = 0

    for i, left in enumerate(left_sort):

        distances += abs(left  - right_sort[i])

    return distances


def calc_similarity(left_col, right_col):
    """Returns the similarity score between two lists"""

    similarity = 0

    for val in left_col:
        similarity += val * right_col.count(val)

    return similarity


def cli_main(filename, part2):
    """main entry"""

    left_col, right_col = read_input_cols(filename)

    if part2:
        similarity = calc_similarity(left_col, right_col)
        print('similarity: %d' % similarity)
    else:
        distances = calc_distance(left_col, right_col)
        print('distances: %d' % distances)


if __name__ == '__main__':

    args = parse_args()
    cli_main(args.filename, args.part2)



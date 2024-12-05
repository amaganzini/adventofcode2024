import argparse
import re

def parse_args():
    """Returns args, wrapper for ArgumentParser config and call"""

    parser = argparse.ArgumentParser(
            prog='day3.py',
            description='Advent of Code day 3')

    parser.add_argument('filename',
                        help='input filename')
    parser.add_argument('-2', '--part2', action='store_true', default=False,
                        help='perform part 2 of the puzzle!')

    args = parser.parse_args()

    return args


def read_muls(filename):
    """Returns all the valid mul()'s in a file"""

    muls = []
    muls_append = muls.append

    r_mul = re.compile(r'mul\((\d+),(\d+)\)')

    for line in open(filename, 'r'):
        muls += r_mul.findall(line)

    return muls


def read_do_muls(filename):
    """Returns all the valid ENABLED mul()'s in a file"""

    r_do = re.compile(r'do\(\)')
    r_dont = re.compile(r'don\'t\(\)')
    r_mul = re.compile(r'mul\((\d+),(\d+)\)')

    enabled_segments = []
    muls = []

    buf = open(filename, 'r').read()

    #split on every occurance of don't
    dont_splits = r_dont.split(buf)

    #start is enabled
    enabled_segments += [dont_splits.pop(0)]

    #split the don't splits by do
    for i, segment in enumerate(dont_splits):

        do_split = r_do.split(segment)

        #after splitting the splits that start with don't() on do(), every split after the first is valid
        enabled_segments += do_split[1::]

    #for segment in enabled_segments:
    for segment in enabled_segments:
        muls += r_mul.findall(segment)

    return muls


def process_muls(muls):
    """returns the processed sum of a list of mul instructions"""

    total = 0

    for a, b in muls:
        total += (int(a) * int(b))

    return total


def cli_main(args):
    """main entry"""

    if args.part2:
        muls = read_do_muls(args.filename)
    else:
        muls = read_muls(args.filename)

    mul_val = process_muls(muls)

    print('total of all muls: %d' % mul_val)


if __name__ == '__main__':

    args = parse_args()
    cli_main(args)



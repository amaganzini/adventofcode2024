import argparse
import re

def parse_args():
    """Returns args, wrapper for ArgumentParser config and call"""

    parser = argparse.ArgumentParser(
            prog='day3.py',
            description='Advent of Code day 3')

    parser.add_argument('filename',
                        help='input filename')

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


def process_muls(muls):
    """returns the processed sum of a list of mul instructions"""

    total = 0

    for a, b in muls:
        total += (int(a) * int(b))

    return total


def cli_main(args):
    """main entry"""

    muls = read_muls(args.filename)

    mul_val = process_muls(muls)

    print('total of all muls: %d' % mul_val)


if __name__ == '__main__':

    args = parse_args()
    cli_main(args)



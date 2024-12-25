import argparse
import re

def parse_args():
    """Returns args, wrapper for ArgumentParser config and call"""

    parser = argparse.ArgumentParser(
            prog='day6.py',
            description='Advent of Code day 6')

    parser.add_argument('filename',
                        help='input filename')
    parser.add_argument('-2', '--part2', action='store_true', default=False,
                        help='perform part 2 of the puzzle!')

    args = parser.parse_args()

    return args


def cli_main(args):
    """main entry"""

    print('filename: %s' % (args.filename))


if __name__ == '__main__':

    args = parse_args()
    cli_main(args)



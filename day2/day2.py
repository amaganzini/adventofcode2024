import argparse

def parse_args():
    """Returns args, wrapper for ArgumentParser config and call"""

    parser = argparse.ArgumentParser(
            prog='day2.py',
            description='Advent of Code day 2')

    parser.add_argument('filename',
                        help='input filename')
    parser.add_argument('-2', '--part2', action='store_true', default=False,
                        help='perform part 2 of the puzzle!')

    args = parser.parse_args()

    return args


def read_input_reports(filename):
    """Returns the reports read from input.txt"""

    return [[int(x) for x in line.split()] for line in open(filename, 'r')]


def check_report_crease(report):
    """Returns whether or not a report is purely increasing or decreasing"""

    sorted_report = sorted(report)
    return report == sorted_report or report == sorted_report[::-1]


MIN_MAGNITUDE = 1
MAX_MAGNITUDE = 3
def check_report_magnitude(report):
    """Returns whether or not a report is changing by an acceptable value"""

    for i in range(len(report) - 1):

        magnitude = abs(report[i] - report[i + 1])

        if magnitude < MIN_MAGNITUDE or magnitude > MAX_MAGNITUDE:
            return False

    return True


def safe_with_a_removal(report):
    """Returns whether the report would be safe if 1 level was removed"""

    for i in range(len(report)):

        new_report = report[:i] + report[i+1:]

        if check_report_crease(new_report) and check_report_magnitude(new_report):
            return True

    return False


def count_safe_reports(reports, part2):
    """Returns the number of safe reports"""

    safe_count = 0

    for report in reports:

        if check_report_crease(report) and check_report_magnitude(report):
            safe_count += 1
        elif part2 and safe_with_a_removal(report):
            safe_count += 1

    return safe_count


def cli_main(filename, part2):
    """main entry"""

    reports = read_input_reports(filename)

    safe_reports = count_safe_reports(reports, part2)

    print('%d safe reports found' % safe_reports)


if __name__ == '__main__':

    args = parse_args()
    cli_main(args.filename, args.part2)



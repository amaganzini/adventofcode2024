import argparse
import re

def parse_args():
    """Returns args, wrapper for ArgumentParser config and call"""

    parser = argparse.ArgumentParser(
            prog='day5.py',
            description='Advent of Code day 5')

    parser.add_argument('filename',
                        help='input filename')
    parser.add_argument('-2', '--part2', action='store_true', default=False,
                        help='perform part 2 of the puzzle!')

    args = parser.parse_args()

    return args


def correct_invalid_update(rules, update):
    """Returns a corrected update based on the rules"""

    corrected_update = update.copy()

    for early, late in rules.items():

        #if the early part of the rule is in the update
        if early in corrected_update:
            early_index = corrected_update.index(early)

            #make sure every late val is after it
            for late_val in late:

                if late_val in corrected_update:

                    late_index = corrected_update.index(late_val)

                    #if we find an offending late
                    if late_index < early_index:

                        #we need to move the early in front!
                        corrected_update.pop(early_index)
                        corrected_update.insert(corrected_update.index(late_val), early)
                        
                        #update early_index since we still need it
                        early_index = corrected_update.index(early)
                        
    return corrected_update


def check_valid_update(rules, update):
    """Returns if an update is valid"""

    for early, late in rules.items():

        #if the early part of the rule is in the update
        if early in update:
            early_index = update.index(early)

            #make sure every late val is after it
            for late_val in late:

                if late_val in update and update.index(late_val) < early_index:
                    return False

    return True


def count_valid_middle_update_numbers(rules, updates, corrected_only):
    """Returns the sum of all the valid update's middle numbers"""

    total = 0

    for update in updates:

        if corrected_only:
            if not check_valid_update(rules, update):
                corrected_update = correct_invalid_update(rules, update)
                total += int(corrected_update[int(len(corrected_update)/2)])

        else:
            if check_valid_update(rules, update):
                #add the middle value in update
                total += int(update[int(len(update)/2)])

    return total


def read_rules_and_updates(filename):
    """Returns the rules and a list of updates from a file"""

    rules = {}
    updates = []

    r_rule = re.compile(r'^(\d+)\|(\d+)')
    r_update = re.compile(r'(\d+)[,\n]')

    for line in open(filename, 'r'):

        read_rule = r_rule.match(line)

        #if we read a rule
        if(read_rule is not None):
            early, late = read_rule.groups()

            if rules.get(early) is None:
                rules[early] = [late]
            elif not late in rules[early]:
                rules[early].append(late)

        else:

            read_update = r_update.findall(line)

            #if we read an update
            if(len(read_update) > 0):
                updates.append(read_update)

    return rules, updates


def cli_main(args):
    """main entry"""

    rules, updates = read_rules_and_updates(args.filename)

    value = count_valid_middle_update_numbers(rules, updates, args.part2)

    print('Total sum of %s middle updates: %d' % ('invalid corrected' if args.part2 else 'valid', value))


if __name__ == '__main__':

    args = parse_args()
    cli_main(args)



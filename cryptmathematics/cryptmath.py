"Crypt mathematics solver in python"
# Author: Argha Sen
# Start Date : 20th December 2014
import string
import re
import itertools

def valid(formula):
    "Validate a formula: No leading zeros. numbers with leading \
    zeors are treatd as octals"
    try:
        return not re.search(r'\b0[0-9]', formula) and eval(formula) is True
    except ArithmeticError:
        return False


def solve(formula):
    "given formula, fill digits to solve it"
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    "generate fillings of letters with digits in formula"
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

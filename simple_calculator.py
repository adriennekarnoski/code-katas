"""simple calculator

Your function will accept three arguments:
The first and second argument will be numbers.
The third argument will represent a sign indicating the operation to perform
on these two numbers.

#1 Best Practices Solution by DigitSo (plus 62 more warriors):

def calculator(x,y,op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        return "unknown value"

"""


def calculator(x, y, op):
    """take the parameters and do math on them."""
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    if op == '*':
        return x * y
    elif op == '/':
        return float(x) / float(y)
    else:
        return "unknown value"
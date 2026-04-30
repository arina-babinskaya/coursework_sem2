from .halstead_operators import get_operators
from .halstead_operands import get_operands


def calculate(node):
    operators = get_operators(node)
    operands = get_operands(node)

    N1 = len(operators)
    N2 = len(operands)

    return N1 + N2
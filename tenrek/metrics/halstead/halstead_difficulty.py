from .halstead_operators import get_operators
from .halstead_operands import get_operands

def calculate(node):
    operators = get_operators(node)
    operands = get_operands(node)

    n1 = len(set(operators))
    n2 = len(set(operands))
    N2 = len(operands)

    if n2 == 0:
        return 0

    return (n1 / 2) * (N2 / n2)
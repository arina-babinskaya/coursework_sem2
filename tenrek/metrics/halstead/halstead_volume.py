import math
from .halstead_uniq_elements import calculate as uniq_els_calc
from .halstead_all_elements import calculate as all_els_calc

def calculate(node):
    n = uniq_els_calc(node)
    N = all_els_calc(node)

    if n == 0:
        return 0

    return N * math.log2(n)
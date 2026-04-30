from .halstead_volume import calculate as volume_calc
from .halstead_difficulty import calculate as difficulty_calc


def calculate(node):
    V = volume_calc(node)
    D = difficulty_calc(node)

    return D * V
from metrics.halstead.halstead_volume import calculate as volume
from .cyclomatic import calculate as cc
from .loc import calculate as loc
import math


def calculate(node):
    V = volume(node)
    CC = cc(node)
    LOC = loc(node)

    MI = (171 - 5.2 * math.log(V) - 0.23 * CC - 16.2 * math.log(LOC))*100 / 171
    return max(0, MI)
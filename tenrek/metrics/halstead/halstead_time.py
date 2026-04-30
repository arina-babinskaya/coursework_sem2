from .halstead_effort import calculate as effort_calc


def calculate(node):
    E = effort_calc(node)
    return E / 18 if E else 0
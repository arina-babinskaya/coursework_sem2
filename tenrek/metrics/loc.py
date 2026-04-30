from clang.cindex import CursorKind

def calculate(node):
    start = node.extent.start.line
    end = node.extent.end.line
    return end - start + 1
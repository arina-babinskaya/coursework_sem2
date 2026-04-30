from clang.cindex import CursorKind

def calculate(node):
    def visit(n, depth):
        max_depth = depth

        if n.kind in [
            CursorKind.IF_STMT,
            CursorKind.FOR_STMT,
            CursorKind.WHILE_STMT,
            CursorKind.SWITCH_STMT
        ]:
            depth += 1

        for child in n.get_children():
            max_depth = max(max_depth, visit(child, depth))

        return max_depth

    return visit(node, 0)
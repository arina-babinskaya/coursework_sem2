from clang.cindex import CursorKind, TokenKind


BRANCH_NODES = {
    CursorKind.IF_STMT,
    CursorKind.FOR_STMT,
    CursorKind.WHILE_STMT,
    CursorKind.DO_STMT,
    CursorKind.SWITCH_STMT,
    CursorKind.CXX_TRY_STMT,
    CursorKind.CXX_CATCH_STMT
}

LOGICAL_OPERATORS = {
    "&&",
    "||"
}


def logical_operators(node):
    count = 0
    tokens = list(node.get_tokens())

    for t in tokens:
        if t.spelling == "&&" or t.spelling == "||":
            count += 1

    return count


def is_else_if(node):
    parent = node.semantic_parent
    if not parent:
        return False

    if parent.kind == CursorKind.IF_STMT:
        children = list(parent.get_children())
        if len(children) >= 2 and children[1] == node:
            return True

    return False


def calculate(root):
    def visit(node, depth):
        complexity = 0
        new_depth = depth

        if node.kind in BRANCH_NODES:
            if node.kind == CursorKind.IF_STMT and is_else_if(node):
                complexity += 1
            else:
                complexity += 1 + depth
                new_depth += 1

        if node.kind == CursorKind.CASE_STMT:
            complexity += 1

        if node.kind == CursorKind.IF_STMT:
            complexity += logical_operators(node)

        if node.kind == CursorKind.CONDITIONAL_OPERATOR:
            complexity += 1 + depth

        if node.kind in (CursorKind.BREAK_STMT, CursorKind.CONTINUE_STMT):
            complexity += 1

        for child in node.get_children():
            complexity += visit(child, new_depth)

        return complexity

    return visit(root, 0)
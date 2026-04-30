from clang.cindex import CursorKind

BRANCH_NODES = {
    CursorKind.IF_STMT,
    CursorKind.FOR_STMT,
    CursorKind.CXX_FOR_RANGE_STMT,
    CursorKind.WHILE_STMT,
    CursorKind.DO_STMT,
    CursorKind.CASE_STMT,
    CursorKind.DEFAULT_STMT,
    CursorKind.CONDITIONAL_OPERATOR,
    CursorKind.CXX_TRY_STMT,
}

LOGICAL_OPERATORS = {
    "&&",
    "||"
}


def is_logical_operator(node):
    if node.kind != CursorKind.BINARY_OPERATOR:
        return False

    for t in node.get_tokens():
        if t.spelling == "&&" or t.spelling == "||":
            return True
    return False


def calculate(node):
    complexity = 1

    def visit(n):
        nonlocal complexity #for accumulating

        if n.kind in BRANCH_NODES:
            complexity += 1

        if n.kind == CursorKind.CXX_CATCH_STMT:
            complexity += 1

        if is_logical_operator(n):
            complexity += 1

        if n.kind == CursorKind.LAMBDA_EXPR:
            complexity += calculate_lambda(n)
            return  # do not need go insite twice

        if n.kind == CursorKind.IF_STMT: # if constexpr
            try:
                if n.is_constexpr():
                    complexity += 1
            except:
                pass

        for child in n.get_children():
            visit(child)

    visit(node)
    return complexity


def calculate_lambda(node): # lambda is count separately
    complexity = 1

    for n in node.walk_preorder():
        if n.kind in BRANCH_NODES:
            complexity += 1

        if n.kind == CursorKind.CXX_CATCH_STMT:
            complexity += 1

        if is_logical_operator(n):
            complexity += 1

    return complexity
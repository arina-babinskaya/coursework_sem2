from clang.cindex import TokenKind, CursorKind

def get_operands(node):
    operands = []

    TYPE_KEYWORDS = {
        'void', 'char', 'short', 'int', 'long', 'float', 'double', 
        'signed', 'unsigned', 'bool', '_Bool', 'complex'
    }

    for t in node.get_tokens():
        if t.kind == TokenKind.LITERAL:
            operands.append(t.spelling)

        elif t.kind == TokenKind.KEYWORD and t.spelling in TYPE_KEYWORDS:
            operands.append(t.spelling)
        
        elif t.kind == TokenKind.IDENTIFIER:
            cursor = t.cursor
            if cursor.kind in {
                CursorKind.TYPE_REF,
                CursorKind.STRUCT_DECL,
                CursorKind.CLASS_DECL,
                CursorKind.TYPEDEF_DECL,
                CursorKind.ENUM_DECL
            }:
                operands.append(t.spelling)
            else:
                operands.append(t.spelling)
    return operands

